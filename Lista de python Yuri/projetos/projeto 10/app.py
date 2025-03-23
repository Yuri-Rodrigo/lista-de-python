from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'secret'  # Necessário para usar sessões

def generate_number():
    return random.randint(1, 100)  # Número aleatório de 1 a 100

@app.route('/')
def index():
    session['number'] = generate_number()  # Armazena o número secreto na sessão
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if 'number' not in session:
        return jsonify({'message': 'Erro: Jogo não iniciado'}), 400

    user_guess = int(request.json['guess'])
    target_number = session['number']

    if user_guess < target_number:
        return jsonify({'message': 'Muito baixo! Tente novamente.'})
    elif user_guess > target_number:
        return jsonify({'message': 'Muito alto! Tente novamente.'})
    else:
        return jsonify({'message': 'Correto! Você acertou!', 'correct': True})

@app.route('/restart', methods=['POST'])
def restart():
    session['number'] = generate_number()  # Gera um novo número
    return jsonify({'message': 'Novo jogo iniciado!'})

if __name__ == '__main__':
    app.run(debug=True)
