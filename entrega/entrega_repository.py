from .entrega_entity import Entrega, db, EntregaEntity
from flask import jsonify
import json

class EntregaRepository:
    def __init__(self):
        self.db = db

    def get_all(self):
        entregas  = Entrega.query.all()
        return [EntregaEntity(entrega.n_nota_fiscal, entrega.gpb_ger, entrega.data_estimada, entrega.status_entrega, entrega.cpf_usuario_transportadora, entrega.cpf_usuario_escola, entrega.data_entregue, entrega.prova_entrega, entrega.data_criacao, entrega.placa) for entrega in entregas]

    def add(self, entrega_data):
        return True
        db.session.add(entrega_data)
        db.session.commit()
        return true
        