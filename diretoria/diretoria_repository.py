from .diretoria_entity import Diretoria, db
from sqlalchemy.orm import joinedload



class DiretoriaRepository:
    def __init__(self):
        self.db = db

    def get_all(self):
        diretorias = Diretoria.query.all()
        return diretorias
    
    def get_by_name(self, nome_diretoria):
        diretoria = Diretoria.query.options(joinedload(Diretoria.escolas)).filter_by(nome=nome_diretoria).first()
        return diretoria
