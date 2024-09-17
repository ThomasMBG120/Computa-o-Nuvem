from flask import Flask
import random

app = Flask(__name__)

# Lista de frases que serão exibidas na página
frases = [
    "Eu amo essa aula!",
    "o Professor é mais novo que o Pablo!", ''
    "Eu sou um Jedi!"]

@app.route('/')
def home():
    frase_aleatoria = random.choice(frases)
    cores = ["red", "Blue", "Green", "Yellow", "Purple", "Orange"]
    cor_aleatoria = random.choice(cores)
    return f"<h1 style='color:{cor_aleatoria};'>{frase_aleatoria}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
