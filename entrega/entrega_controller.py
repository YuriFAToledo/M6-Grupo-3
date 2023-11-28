from flask import Blueprint, jsonify, request
from .entrega_service import EntregaService

class EntregaController:
    def __init__(self):
        self.service = EntregaService()
        self.bp = Blueprint('entrega_controller', __name__)

        self.bp.route('/entregas', methods=['GET'])(self.get_entregas)
        self.bp.route('/entrega', methods=['POST'])(self.add_entrega)

    def get_entregas(self):
        entregas = self.service.get_all_entregas()
        return jsonify(entregas)

    def add_entrega(self):
        entrega_data = request.json
        self.service.add_entrega(entrega_data)
        return jsonify({"message": "entrega added successfully"}), 201
