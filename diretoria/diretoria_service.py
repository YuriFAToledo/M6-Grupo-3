from .diretoria_repository import DiretoriaRepository

class DiretoriaService:
    def __init__(self):
        self.repository = DiretoriaRepository()

    def get_all_diretorias(self):
        diretorias = self.repository.get_all()
        return [self.to_dict(diretoria) for diretoria in diretorias]
    
    def get_diretoria_by_name(self, nome_diretoria):
        diretoria = self.repository.get_by_name(nome_diretoria)
        return self.to_dict(diretoria) if diretoria else None

    def to_dict(self, diretoria):
        return{
            'nome': diretoria.nome,
            'regiao': diretoria.regiao,
            'escolas': [escola.to_dict() for escola in diretoria.escolas]
        }