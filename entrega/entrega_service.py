from .entrega_repository import EntregaRepository

class EntregaService:
    def __init__(self):
        self.repository = EntregaRepository()

    def get_all_entregas(self):
        entregas = self.repository.get_all()
        return [self.to_dict(entrega) for entrega in entregas]

    def add_entrega(self, entrega_data):
        self.repository.add(entrega_data)

    def to_dict(self, entrega):
        return {
            'n_nota_fiscal': entrega.n_nota_fiscal,
            'gpb_ger': entrega.gpb_ger,
            'data_estimada': entrega.data_estimada,
            'status_entrega': entrega.status_entrega,
            'cpf_usuario_transportadora': entrega.cpf_usuario_transportadora,
            'cpf_usuario_escola': entrega.cpf_usuario_escola,
            'data_entregue': entrega.data_entregue,
            'prova_entrega': entrega.prova_entrega,
            'data_criacao': entrega.data_criacao,
            'placa': entrega.placa,
        }