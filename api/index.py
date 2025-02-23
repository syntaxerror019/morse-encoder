from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encode')
def encode():
    return render_template('encode.html')

@app.route('/decode')
def decode():
    return render_template('decode.html')

@app.route('/beacon')
def beacon():
    return render_template('beacon.html')