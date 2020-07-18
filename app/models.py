from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(130), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    
    def __init__(self, name, email, password):
        self.name=name
        self.email=email
        self.password = generate_password_hash(password)
        
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
        
        
class Cliente(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    celular = db.Column(db.String(20))
    email = db.Column(db.String(150))
    
    def __init__(self, nome, cidade, telefone, celular, email):
        self.nome=nome
        self.cidade=cidade
        self.telefone=telefone
        self.celular
        self.email=email
    
    def __repr__(self):
        return '{}'.format(self.nome)
        
  
class Grupo(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100))
    
    def __init__(self, nome):
        self.nome = nome
        
    def __repr__(self):
        return '{}'.format(self.nome)
        
class Categoria(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100))
    
    def __init__(self, nome):
        self.nome = nome
        
    def __repr__(self):
        return '{}'.format(self.nome)
        
        
class Endereco(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    endereco = db.Column(db.String(200))
    numero = db.Column(db.String(50))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(2))
    cep = db.Column(db.String(10))
    
    
    def __init__(self, endereco, numero, bairro, cidade, estado, cep):
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        
    def __repr__(self):
        return '{}'.format(self.endereco)


class Assinante(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'),
        nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'),
        nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('endereco.id'),
        nullable=False)
    codigo_assinante = db.Column(db.String(100), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))
    celular = db.Column(db.String(20))
    email = db.Column(db.String(150))
    
    def __init__(self, grupo_id, categoria_id, endereco_id, codigo_assinante, nome, telefone, celular, email):
        self.grupo_id = grupo_id
        self.categoria_id = categoria_id
        self.endereco_id = endereco_id
        self.codigo_assinante = codigo_assinante
        self.nome = nome
        self.telefone = telefone
        self.celular = celular
        self.email = email
        
    def __repr__(self):
        return '{}'.format(self.nome)
    

        
db.create_all()