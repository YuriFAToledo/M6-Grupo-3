from .transportadora_entity import Transportadora, db
from flask import jsonify
import json

class TransportadoraRepository:
    def __init__(self):
        self.db = db

    def get_all(self):
        transportadoras = Transportadora.query.all()
        return transportadoras

    def add(self, transportadora_data):
        transportadora = Transportadora(
            cnpj=transportadora_data['cnpj'],
            nome=transportadora_data['nome'],
            logradouro=transportadora_data['logradouro'],
            numero=transportadora_data['numero'],
            bairro=transportadora_data['bairro'],
            cep=transportadora_data['cep']
        )
        db.session.add(transportadora)
        db.session.commit()
        return True

    def get_by_cnpj(self, cnpj):
        transportadora = Transportadora.query.filter_by(cnpj=cnpj).first()
        return transportadora

    def update(self, transportadora_data):
        transportadora = Transportadora.query.filter_by(cnpj=transportadora_data['cnpj']).first()
        transportadora.nome = transportadora_data['nome']
        transportadora.logradouro = transportadora_data['logradouro']
        transportadora.numero = transportadora_data['numero']
        transportadora.bairro = transportadora_data['bairro']
        transportadora.cep = transportadora_data['cep']
        db.session.commit()
        return True

    def delete(self, cnpj):
        transportadora = Transportadora.query.filter_by(cnpj=cnpj).first()
        db.session.delete(transportadora)
        db.session.commit()
        return True