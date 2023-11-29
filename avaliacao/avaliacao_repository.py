from .avaliacao_entity import Avaliacao, db
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
        # new_avaliacao = Avaliacao(**avaliacao_data)
        # db.session.add(avaliacao_data)
        # db.session.commit()
        # return avaliacao_data
        return avaliacao_data