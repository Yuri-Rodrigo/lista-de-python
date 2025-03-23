from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("principal"))

@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/novocadastro", methods=["GET", "POST"])
def novocadastro():

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        # banco de dados
        return render_template("novocadastro.html", nome=nome, email=email, telefone=telefone)

@app.route("/relatorio")
def relatorio():
    return render_template("relatorio.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)