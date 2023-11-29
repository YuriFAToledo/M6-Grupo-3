from .avaliacao_entity import Avaliacao, db
# TODO adicionar metodo para verificar se a entrega existe na service e trocar no lugar da entity
from entrega.entrega_entity import Entrega
from flask import jsonify
import json

class AvaliacaoRepository:
    def __init__(self):
        self.db = db

    def get_all(self):
        avaliacoes = Avaliacao.query.all()
        return avaliacoes
    
    def get_by_n_nota_fiscal(self, n_nota_fiscal):
        avaliacao = Avaliacao.query.filter_by(n_nota_fiscal=n_nota_fiscal).first()
        return avaliacao

    def add(self, avaliacao_data):
        entrega_existente = Entrega.query.filter_by(n_nota_fiscal=avaliacao_data['n_nota_fiscal']).first()
        if entrega_existente: 
            new_avaliacao = Avaliacao(**avaliacao_data)
            db.session.add(new_avaliacao)
            db.session.commit()
            return new_avaliacao
        else: 
            return False