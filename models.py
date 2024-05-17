from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  # Definindo explicitamente o nome da tabela

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    estado_civil = db.Column(db.String(50))
    rua = db.Column(db.String(200))
    numero = db.Column(db.Integer)
    bairro = db.Column(db.String(100))
    rg = db.Column(db.String(20))
    cpf = db.Column(db.String(20))
    telefone = db.Column(db.String(20))
    tem_filho = db.Column(db.Boolean, default=False, nullable=False)
    numero_filhos = db.Column(db.Integer)
    conjuge_nome = db.Column(db.String(100))
    conjuge_cpf = db.Column(db.String(20))
    conjuge_rg = db.Column(db.String(20))
    conjuge_data_nascimento = db.Column(db.Date)
    gestante = db.Column(db.Boolean, default=False, nullable=False)
    retirada_cesta = db.Column(db.Date)
    proxima_cesta = db.Column(db.Date)

    def __repr__(self):
        return f'<User {self.nome}>'

    def calculate_next_basket_date(self):
        """Calcula a próxima data de retirada da cesta baseada no status de gestante do usuário."""
        if self.gestante:
            self.proxima_cesta = self.retirada_cesta + timedelta(days=30)
        else:
            self.proxima_cesta = self.retirada_cesta + timedelta(days=60)

class Filho(db.Model):
    __tablename__ = 'filhos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    rg = db.Column(db.String(9), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    usuario = db.relationship('User', backref=db.backref('filhos', lazy=True))

    def __repr__(self):
        return f'<Filho {self.nome}>'
