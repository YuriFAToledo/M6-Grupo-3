from flask import Blueprint, jsonify, request
from .diretoria_service import DiretoriaService

class DiretoriaController:
    def __init__(self):
        self.service = DiretoriaService()
        self.bp = Blueprint('diretoria_controller', __name__)

        self.bp.route('/diretorias', methods = ['GET'])(self.get_diretorias)
        self.bp.route('/diretoria/<string:nome_diretoria>', methods = ['GET'])(self.get_diretoria_by_name)

    def get_diretorias(self):
        diretorias = self.service.get_all_diretorias()
        return jsonify(diretorias), 200
    
    def get_diretoria_by_name(self, nome_diretoria):
        diretoria = self.service.get_diretoria_by_name(nome_diretoria)
        return jsonify(diretoria), 200
        
