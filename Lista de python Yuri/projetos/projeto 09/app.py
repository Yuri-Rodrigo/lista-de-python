from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        largura_terreno = float(request.form['largura_terreno'])
        profundidade_terreno = float(request.form['profundidade_terreno'])
        largura_calcada = max(float(request.form['largura_calcada']), 1.2)
        altura_concreto = max(float(request.form['altura_concreto']), 0.06)

        # Calculando a área da calçada na frente do terreno
        area_calcada = largura_terreno * largura_calcada
        
        # Calculando o volume de concreto necessário
        volume_concreto = area_calcada * altura_concreto
        
        return render_template('resultado.html', 
                               largura_terreno=largura_terreno,
                               profundidade_terreno=profundidade_terreno,
                               largura_calcada=largura_calcada,
                               altura_concreto=altura_concreto,
                               volume_concreto=volume_concreto)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
