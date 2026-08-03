from flask import Flask, render_template, request
import qrcode
import io
import os
import base64
app = Flask(__name__)

def generate(info,file_path):
    qr = qrcode.QRCode()
    qr.add_data(info)
    qr.make(fit=True)
    img = qr.make_image()
    if os.path.isdir(file_path):
        file_path = os.path.join(file_path, 'Qrcode.png')
    elif not file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        file_path += '.png'
    img.save(file_path)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    qr_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return qr_b64

@app.route('/')
def home():
    return render_template('Qrcode.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('text')
    file_name = request.form.get('file')
    code = generate(data,file_name)
    
    return render_template('Qrcode.html', results=code)

if __name__ == '__main__':
    app.run(debug=True)