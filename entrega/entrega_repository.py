from .entrega_entity import Entrega, db
from flask import jsonify
import json

class EntregaRepository:
    def __init__(self):
        self.db = db

    def get_all(self):
        entregas = Entrega.query.all()
        return entregas

    def add(self, entrega_data):
        return True
        db.session.add(entrega_data)
        db.session.commit()
        return true
        