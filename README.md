## **Jogoteca**

Jogoteca é um projeto para gerenciar uma coleção de jogos. O projeto permite que os usuários façam upload de imagens, gerenciem jogos e muito mais.

![Captura de tela 2023-09-10 104258](https://github.com/gsoaresdz/jogoteca/assets/69989654/a31abb3c-d5a3-4b75-9a3f-91ef4dea7821)

---

## **Estrutura do Projeto**

```php
jogoteca/
│
├── config.py                # Configurações do projeto
├── helpers.py               # Funções auxiliares
├── jogoteca.py              # Arquivo principal do projeto
├── models.py                # Modelos de dados
├── prepara_banco.py         # Script para preparar o banco de dados
│
├── static/                  # Arquivos estáticos (CSS, JS, etc.)
├── templates/               # Templates HTML
├── uploads/                 # Pasta para uploads de usuários
│
├── views_game.py            # Lógica de exibição para jogos
└── views_user.py            # Lógica de exibição para usuários

```

---

## **Bibliotecas e Módulos Utilizados**

- **`mysql.connector`**: Para conectar e operar com MySQL.
- **`wtforms`**: Biblioteca para lidar com formulários.
- **`flask_sqlalchemy`**: Extensão Flask para usar SQLAlchemy.
- **`flask_wtf.csrf`**: Para proteção CSRF.
- **`flask_bcrypt`**: Para criptografia.
- **`os`**: Biblioteca padrão do Python para interação com o sistema operacional.
- **`flask`**: Framework web.
- **`time`**: Biblioteca padrão do Python para manipulação de tempo.

---

## **Como Instalar o Python**

1. Acesse **https://www.python.org/downloads/**
2. Escolha a versão do Python que deseja instalar.
3. Siga as instruções na tela para instalação.

---

## **Como Instalar o Visual Studio Code (VSCode)**

1. Acesse **https://code.visualstudio.com/**
2. Clique no botão "Download" correspondente ao seu sistema operacional.
3. Siga as instruções na tela para instalação.
4. Recomendamos a instalação da extensão "Python" do VSCode para melhor desenvolvimento.

---

## **Como Iniciar o Projeto**

1. Clone este repositório ou faça o download.
2. Navegue até a pasta do projeto e crie um ambiente virtual:

```
python -m venv venv
```

1. Ative o ambiente virtual:
- Windows: **`venv\Scripts\activate`**
- Linux/Mac: **`source venv/bin/activate`**
1. Instale as bibliotecas necessárias:

```
pip install -r requirements.txt
```

**Nota**: O arquivo **`requirements.txt`** deve ser criado e conter todas as bibliotecas necessárias.

1. Execute o arquivo principal:

```
python jogoteca.py
```

1. Acesse a aplicação em seu navegador no endereço **http://127.0.0.1:5000/**.
