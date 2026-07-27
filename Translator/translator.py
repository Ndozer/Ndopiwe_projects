from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
app = Flask(__name__)

def translate(lang2, text):
    return GoogleTranslator(source='auto', target=lang2).translate(text)

@app.route('/')
def home():
    return render_template('translator.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('text')
    lang2 = request.form.get('language2')
    translation = translate(lang2, data)
    
    return render_template('translator.html', results=translation)

if __name__ == '__main__':
    app.run(debug=True)