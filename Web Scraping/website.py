import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

def web_scrap(url, element):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    res = requests.get(url, headers=headers, timeout=10)
    res.raise_for_status() 
    
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup.find_all(element)

@app.route('/')
def home():
    return render_template('web_web.html')

@app.route('/submit', methods=['POST'])
def submit():
    url_data = request.form.get('my_url')
    dropdown = request.form.get('elements')

    r_string = ""    
    try:
        results = web_scrap(url_data, dropdown)
        for r in results:
            r_string += r.text + "\n"
        if not r_string.strip():
            r_string = f"Connected successfully, but no <{dropdown}> elements were found."
    except requests.exceptions.Timeout:
        r_string = "Error: The website took too long to respond (Timeout). They might be blocking automated tools."
    except requests.exceptions.HTTPError as e:
        r_string = f"HTTP Error: The website returned status code {e.response.status_code}."
    except requests.exceptions.RequestException as e:
        r_string = f"An error occurred while trying to connect: {str(e)}"
    return render_template('web_web.html', results=r_string)

if __name__ == '__main__':
    app.run(debug=True)