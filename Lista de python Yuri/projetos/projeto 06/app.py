from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar os alunos
alunos = []

@app.route('/')
def home():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']

    # Criar um dicionário com os dados do aluno
    aluno = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'senha': senha
    }

    # Adicionar o aluno à lista
    alunos.append(aluno)

    # Redirecionar para a página de sucesso
    return redirect(url_for('sucesso', nome=nome, email=email, telefone=telefone))

@app.route('/sucesso')
def sucesso():
    nome = request.args.get('nome')
    email = request.args.get('email')
    telefone = request.args.get('telefone')
    return render_template('sucesso.html', nome=nome, email=email, telefone=telefone)

if __name__ == '__main__':
    app.run(debug=True)
