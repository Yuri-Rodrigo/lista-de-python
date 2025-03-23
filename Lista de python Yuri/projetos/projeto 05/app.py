from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def medicoesterreno(largura, comprimento):
    area = largura*comprimento
    perimetro = 2*largura + 2*comprimento
    return area, perimetro

@app.route("/")
def home():
    return redirect(url_for("principal"))

@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route("/calculoterreno", methods=["GET", "POST"])
def calculoterreno():

    if request.method == "POST":
        largura = float(request.form.get("largura"))
        comprimento = float(request.form.get("comprimento"))

        area, perimetro = medicoesterreno(largura, comprimento)

        return render_template("calculoterreno.html",
                               largura=largura,
                               comprimento=comprimento,
                               area=area,
                               perimetro=perimetro )
    
if __name__ == "__main__":
    app.run(debug=True)