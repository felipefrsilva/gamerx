SECRET_KEY = 'secreto'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '10975468*',
        servidor = 'localhost',
        database = 'jogoteca'
    )