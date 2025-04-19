from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rankings")
def rankings():
    return render_template("rankings.html")

@app.route("/graficos")
def graficos():
    return render_template("graficos.html")

@app.route("/artigos")
def artigos():
    return render_template("artigos.html")

@app.route("/pesquisa")
def pesquisa():
    return render_template("pesquisa.html")

if __name__ == "__main__":
    app.run(debug=True)
