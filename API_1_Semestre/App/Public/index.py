from flask import Flask
index = Flask(__index__)
@index.route('/')
def home():
    return "Olá, mundo!"
if __index__ == '__main__':
    index.run(debug=True)