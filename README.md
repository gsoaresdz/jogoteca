<h1 align="center">Jogoteca</h1>
<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/gsoaresdz/jogoteca?color=56BEB8">
  <img alt="Github language count" src="https://img.shields.io/github/languages/count/gsoaresdz/jogoteca?color=56BEB8">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/gsoaresdz/jogoteca?color=56BEB8">
  <!--<img alt="License" src="https://img.shields.io/github/license/usuario/jogoteca?color=56BEB8">-->
</p>
<p align="center">
  <a href="#dart-sobre">Sobre</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-tecnologias">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requerimentos">Requerimentos</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-execução">Execução</a> &#xa0; | &#xa0;
  <a href="#memo-licença">Licença</a> &#xa0; | &#xa0;
  <a href="https://github.com/gsoaresdz" target="_blank">Autor</a>
</p>
<br>

## **:dart: Sobre**

Este projeto consiste em uma aplicação web chamada Jogoteca, que permite aos usuários cadastrar, visualizar e gerenciar informações sobre jogos. A aplicação utiliza o framework Flask para o desenvolvimento web e inclui funcionalidades de autenticação de usuários, upload de imagens e manipulação de banco de dados.

## **:memo: Estrutura do Projeto**

A estrutura do projeto é organizada da seguinte forma:

- **config.py:** Configurações da aplicação.
- **helpers.py:** Funções auxiliares.
- **jogoteca.py:** Arquivo principal da aplicação.
- **models.py:** Definição dos modelos do banco de dados.
- **prepara_banco.py:** Script para preparar o banco de dados.
- **static:** Arquivos estáticos (CSS, JS, imagens).
- **templates:** Templates HTML.
- **uploads:** Diretório para uploads de imagens.
- **views_game.py:** Views relacionadas aos jogos.
- **views_user.py:** Views relacionadas aos usuários.

## **:sparkles: Features**

:heavy_check_mark: **Feature 1**: Cadastro e autenticação de usuários.

:heavy_check_mark: **Feature 2**: Cadastro, visualização e gerenciamento de jogos.

:heavy_check_mark: **Feature 3**: Upload de imagens para os jogos.

:heavy_check_mark: **Feature 4**: Interface amigável utilizando templates HTML.

## **:rocket: Tecnologias**

As seguintes ferramentas foram usadas neste projeto:

- [Python](https://www.python.org/)
- Flask
- SQLite
- Jinja2
- Werkzeug

## **:white_check_mark: Requerimentos**

Antes de iniciar :checkered_flag:, você precisa ter [Git](https://git-scm.com/) e [Python](https://www.python.org/) instalados.

## **:checkered_flag: Execução**

```bash
bashCopy code
# Clone do projeto
$ git clone https://github.com/gsoaresdz/jogoteca.git

# Entre no diretório do projeto
$ cd jogoteca

# Crie um ambiente virtual
$ python -m venv venv

# Ative o ambiente virtual
$ source venv/bin/activate  # No Windows use `venv\Scripts\activate`

# Instale as dependências
$ pip install -r requirements.txt

# Prepare o banco de dados
$ python prepara_banco.py

# Execute a aplicação
$ flask run

# A aplicação estará disponível em http://127.0.0.1:5000

```

## **:memo: Licença**

Este projeto está sob licença do MIT. Para obter mais detalhes, consulte o arquivo [LICENSE](LICENSE).

Feito com :heart: by <a href="https://github.com/gsoaresdz" target="_blank">gsoaresdz</a>

&#xa0;

<a href="#top">De volta ao topo</a>
