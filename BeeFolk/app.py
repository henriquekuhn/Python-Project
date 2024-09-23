from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)  # Inicializa o Bootstrap5 no app

@app.route('/')
def home():
    return render_template('include.html')

@app.route('/calculator', methods=['POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            OG = float(request.form['OG'])
            FG = float(request.form['FG'])
            result = (76.08 * (OG - FG) / (1.775 - OG)) * (FG / 0.794)
            result = f"{result:.4f}"  # Formata o resultado para 4 casas decimais
        except ValueError:
            result = "Erro: por favor, insira números válidos."
    return f'<h3 class="display-result">Result: {result}</h3>'

if __name__ == '__main__':
    app.run(debug=True)
