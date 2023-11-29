from flask import Blueprint, jsonify, request
from .transportadora_service import TransportadoraService

class TransportadoraController:
    def __init__(self):
        self.service = TransportadoraService()
        self.bp = Blueprint('transportadora_controller', __name__)

        self.bp.route('/transportadora', methods=['POST'])(self.add_transportadora)
        self.bp.route('/transportadoras', methods=['GET'])(self.get_transportadoras)
        self.bp.route('/transportadora/<string:cnpj>', methods=['GET'])(self.get_transportadora_by_cnpj)
        self.bp.route('/transportadora', methods=['PATCH'])(self.update_transportadora)
        self.bp.route('/transportadora/<string:cnpj>', methods=['DELETE'])(self.delete_tranportadora)
    
    def add_transportadora(self):
        transportadora_data = request.json
        self.service.add_transportadora(transportadora_data)
        return jsonify({"message": "transportadora added successfully"}), 201
    
    def get_transportadoras(self):
        return self.service.get_all_transportadoras()
    
    def get_transportadora_by_cnpj(self, cnpj):
        transportadora_cnpj = cnpj
        return self.service.get_transportadora_by_cnpj(transportadora_cnpj)
    
    def update_transportadora(self):
        transportadora_data = request.json
        self.service.update_transportadora(transportadora_data)
        return jsonify({"message": "transportadora updated successfully"}), 201
    
    def delete_tranportadora(self, cnpj):
        transportadora_cnpj = cnpj
        self.service.delete_transportadora(transportadora_cnpj)
        return jsonify({"message": "transportadora deletec successfully"}), 201