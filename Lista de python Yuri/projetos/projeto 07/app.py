from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de livros (simulando um banco de dados simples)
livros = []

@app.route('/')
def index():
    return render_template('index.html', livros=livros)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano = request.form['ano']
        livros.append({'titulo': titulo, 'autor': autor, 'ano': ano})
        return redirect(url_for('index'))
    return render_template('cadastro.html')

@app.route('/busca')
def busca():
    return render_template('busca.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
