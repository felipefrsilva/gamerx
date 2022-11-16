import os
from main import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, valodators

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [valodators.DataRequired(), valodators.Length(min=1, max=50)])
    categoria = StringField('Categoria', [valodators.DataRequired(), valodators.Length(min=1, max=40)])
    console = StringField('Console', [valodators.DataRequired(), valodators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}.jpg' in nome_arquivo:
            return nome_arquivo

    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))