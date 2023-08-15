SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario = 'root',
        senha = 'root',
        servidor = '127.0.0.1',
        database = 'jogoteca'
    )
