import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import openai
import time

app = Flask(__name__)
client = openai.OpenAI(api_key="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")
def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    answer = response.choices[0].message.content
    return answer
@app.route('/')
def home():
    return render_template('webpage.html')
@app.route('/submit', methods=['POST'])

def submit():
    question = request.form.get('question')
    max_retries = 3
    delay = 2
    for attempt in range(max_retries):
        try:
            answer = ask_ai(question)
            return render_template('webpage.html', results=answer)
        except openai.RateLimitError:
            if attempt < max_retries - 1:
                time.sleep(delay)
                delay *= 2  
                continue
            else:
                answer = "Error: The server is currently busy. Please try again."
        except openai.APIConnectionError:
            answer = "Error: Could not connect to the OpenAI servers."
        except Exception as e:
            answer = f"An unexpected error occurred: {str(e)}"
            break
    return render_template('webpage.html', results=answer)

if __name__ == '__main__':
    app.run(debug=True)