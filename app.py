# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo ao LocalHost Builder! Seu site está no ar localmente.'

if __name__ == '__main__':
    app.run(debug=True)
  
