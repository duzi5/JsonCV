from banco import banco
from app import app
import sqlalchemy




class Curriculo(banco.Model): 
    id = banco.Column(banco.Integer, primary_key = True)
    nome = banco.Column(banco.String(200))
    data_de_nascimento = banco.Column(banco.Date)
    resumo = banco.Column(banco.Text(1000))
    


class Experiencias(banco.Model):
    id = banco.Column(banco.Integer, primary_key = True)
    nome_da_empresa = banco.Column(banco.String(200))
    cargo = banco.Column(banco.String(100))    
    descricao = banco.Column(banco.String(1000))
    data_entrada = banco.Column(banco.Date)
    data_saida = banco.Column(banco.Date)
