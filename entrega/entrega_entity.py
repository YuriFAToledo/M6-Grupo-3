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

class EntregaEntity:

    def __init__(self, n_nota_fiscal, gpb_ger, data_estimada, status_entrega, cpf_usuario_transportadora, cpf_usuario_escola, data_entregue, prova_entrega, data_criacao, placa):
        self._n_nota_fiscal = n_nota_fiscal
        self._gpb_ger = gpb_ger
        self._data_estimada = data_estimada
        self._status_entrega = status_entrega
        self._cpf_usuario_transportadora = cpf_usuario_transportadora
        self._cpf_usuario_escola = cpf_usuario_escola
        self._data_entregue = data_entregue
        self._prova_entrega = prova_entrega
        self._data_criacao = data_criacao
        self._placa = placa

    def to_dict(self):
        return {
            'n_nota_fiscal': self._n_nota_fiscal,
            'gpb_ger': self._gpb_ger,
            'data_estimada': self._data_estimada,
            'status_entrega': self._status_entrega,
            'cpf_usuario_transportadora': self._cpf_usuario_transportadora,
            'cpf_usuario_escola': self._cpf_usuario_escola,
            'data_entregue': self._data_entregue,
            'prova_entrega': self._prova_entrega,
            'data_criacao': self._data_criacao,
            'placa': self._placa,
        }
