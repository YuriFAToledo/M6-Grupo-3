from .transportadora_repository import TransportadoraRepository

class TransportadoraService:
    def __init__(self) -> None:
        self.repository = TransportadoraRepository()
    
    def add_transportadora(self, transportadora_data):
        self.repository.add(transportadora_data)

    def get_all_transportadoras(self):
        transportadoras = self.repository.get_all()
        return [self.to_dict(transportadora) for transportadora in transportadoras]

    def get_transportadora_by_cnpj(self, cnpj):
        transportadora = self.repository.get_by_cnpj(cnpj)
        return self.to_dict(transportadora)

    def update_transportadora(self, transportadora_data):
        self.repository.update(transportadora_data)

    def delete_transportadora(self, cnpj):
        self.repository.delete(cnpj)

    def to_dict(self, transportadora):
        return {
            'cnpj': transportadora.cnpj,
            'nome': transportadora.nome,
            'logradouro': transportadora.logradouro,
            'numero': transportadora.numero,
            'bairro': transportadora.bairro,
            'cep': transportadora.cep,
        }
    


