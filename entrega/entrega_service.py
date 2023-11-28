from .entrega_repository import EntregaRepository

class EntregaService:
    def __init__(self):
        self.repository = EntregaRepository()

    def get_all_entregas(self):
        return [entrega.to_dict() for entrega in self.repository.get_all()]

    def add_entrega(self, entrega_data):
        self.repository.add(entrega_data)
