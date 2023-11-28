from entrega import db

class Entrega(db.Model):
    n_nota_fiscal = db.Column(db.String(255), primary_key=True)
    #    cnpj_fornecedor = db.Column(db.Integer, db.ForeignKey('fornecedor.cnpj'), nullable=False)
    #    cnpj_transportadora = db.Column(db.String(255), db.ForeignKey('transportadora.cnpj'), nullable=False)
    #    cie_escola = db.Column(db.Integer, db.ForeignKey('escola.cie'), nullable=False)
    gpb_ger = db.Column(db.String(255))
    data_estimada = db.Column(db.DateTime)
    status_entrega = db.Column(db.String(255))
    cpf_usuario_transportadora = db.Column(db.String(255))
    cpf_usuario_escola = db.Column(db.String(255))
    data_entregue = db.Column(db.DateTime)
    prova_entrega = db.Column(db.Boolean)
    data_criacao = db.Column(db.DateTime)
    placa = db.Column(db.String(20), nullable=False)
