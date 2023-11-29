from avaliacao import db
from entrega.entrega_entity import Entrega

class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    n_nota_fiscal = db.Column(db.String(255), db.ForeignKey(f'{Entrega.__tablename__}.n_nota_fiscal'), nullable=False)
    avaliacao_entregador = db.Column(db.Integer)
    avaliacao_embalagem = db.Column(db.Integer)
    avaliacao_materiais = db.Column(db.Integer)
    avaliacao_pontualidade = db.Column(db.Integer)
    feedback = db.Column(db.String(255), nullable=True)