from diretoria import db

class Diretoria(db.Model):
    nome = db.Column(db.String(255), primary_key=True)
    regiao = db.Column(db.String(255))
    escolas = db.relationship('Escola', backref='diretoria', lazy='subquery')

class Escola(db.Model):
    cie = db.Column(db.String(255), primary_key=True)
    nome_diretoria = db.Column(db.String(255), db.ForeignKey('diretoria.nome'))
    nome = db.Column(db.String(255))
    logradouro = db.Column(db.String(255))
    numero = db.Column(db.String(255))
    bairro = db.Column(db.String(255))
    cep = db.Column(db.String(255))

    def to_dict(self):
        return {
            'cie': self.cie,
            'nome_diretoria': self.nome_diretoria,
            'nome': self.nome,
            'logradouro': self.logradouro,
            'numero': self.numero,
            'bairro': self.bairro,
            'cep': self.cep
    }

# class DiretoriaEntity:
#     def __init__(self, nome, regiao, escolas):
#         self._nome = nome
#         self._regiao = regiao
#         self._escolas = 

#     def to_dict(self):
#         return{
#             'nome': self._nome,
#             'regiao': self._regiao,
#             'escolas':self._escolas
# }
