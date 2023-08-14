from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from flask_sqlalchemy import SQLAlchemy


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'PC')
jogo2 = Jogo('God of War', 'Rock in Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')

lista = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Gabriel Soares", "GS", "gabriel@alura")
usuario2 = Usuario("João", "JG", "joao@alura")
usuario3 = Usuario("Maria", "MG", "maria@alura")

usuarios = { usuario1.nickname: usuario1, usuario2.nickname: usuario2, usuario3.nickname: usuario3 }

app = Flask(__name__)
app.secret_key = 'alura'

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario = 'root',
        senha = 'root',
        servidor = '127.0.0.1',
        database = 'jogoteca'
    )

@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima = url_for('novo')))
    return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] ==  usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)