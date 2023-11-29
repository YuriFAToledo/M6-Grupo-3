from .avaliacao_repository import AvaliacaoRepository

class AvaliacaoService:
    def __init__(self):
        self.repository = AvaliacaoRepository()

    def get_all_avaliacoes(self):
        avaliacoes = self.repository.get_all()
        return [self.to_dict(avaliacao) for avaliacao in avaliacoes]
    
    def get_by_n_nota_fiscal(self, n_nota_fiscal):
        avaliacao = self.repository.get_by_n_nota_fiscal(n_nota_fiscal)
        return self.to_dict(avaliacao)
    
    def add_avaliacao(self, avaliacao_data):
        response = self.repository.add(avaliacao_data)
        if response:
            return True
        else:
            return False
        
    
    def to_dict(self, avaliacao):
        return {
            'n_nota_fiscal': avaliacao.n_nota_fiscal,
            'avaliacao_entregador': avaliacao.avaliacao_entregador,
            'avaliacao_embalagem': avaliacao.avaliacao_embalagem,
            'avaliacao_materiais': avaliacao.avaliacao_materiais,
            'avaliacao_pontualidade': avaliacao.avaliacao_pontualidade,
            'feedback': avaliacao.feedback,
        }