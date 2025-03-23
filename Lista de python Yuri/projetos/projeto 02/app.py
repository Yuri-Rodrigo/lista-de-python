from flask import Flask, render_template

app = Flask(__name__)

@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/relatorio")
def relatorio():
    return render_template("relatorio.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)