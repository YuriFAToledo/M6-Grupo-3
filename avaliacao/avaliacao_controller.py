from flask import Blueprint, jsonify, request
from .avaliacao_service import AvaliacaoService

class AvaliacaoController:
    def __init__(self):
        self.service = AvaliacaoService()
        self.bp = Blueprint('avaliacao_controller', __name__)

        self.bp.route('/avaliacoes', methods=['GET'])(self.get_avaliacoes)
        self.bp.route('/avaliacao', methods=['POST'])(self.add_avaliacao)
        self.bp.route('/avaliacao/<n_nota_fiscal>', methods=['GET'])(self.get_avaliacao_by_n_nota_fiscal)

    def get_avaliacoes(self):
        avaliacoes = self.service.get_all_avaliacoes()
        return jsonify(avaliacoes)

    def get_avaliacao_by_n_nota_fiscal(self, n_nota_fiscal):
        avaliacao = self.service.get_by_n_nota_fiscal(n_nota_fiscal)
        return jsonify(avaliacao)

    def add_avaliacao(self):
        avaliacao_data = request.json
        teste = self.service.add_avaliacao(avaliacao_data)
        if teste:
            return jsonify({"message": "avaliacao added successfully"}), 201
        else:
            return jsonify({"message": "avaliacao not added, n_nota_fiscal not found"}), 404
        # return jsonify({"message": "avaliacao added successfully"}), 201