from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Armazenamento temporário dos dados de inscrição em uma lista (não recomendado para produção)
inscricoes = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        idade = request.form['idade']
        distancia = request.form['distancia']

        inscricao = {
            'nome': nome,
            'telefone': telefone,
            'email': email,
            'idade': idade,
            'distancia': distancia
        }

        inscricoes.append(inscricao)
        return redirect(url_for('inscricoes'))

    return render_template('index.html')


@app.route('/inscricoes')
def inscricoes():
    return render_template('inscricoes.html', inscricoes=inscricoes)


if __name__ == '__main__':
    app.run(debug=True)
