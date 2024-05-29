from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'cliente'
    clienteid = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(15))
    correoelectronico = db.Column(db.String(50))

class Gabinete(db.Model):
    __tablename__ = 'gabinete'
    gabineteid = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    pais = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(15))
    abogados = db.relationship('Abogado', back_populates='gabinete')

class Abogado(db.Model):
    __tablename__ = 'abogado'
    abogadoid = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(100))
    telefono =db. Column(db.String(15))
    correoelectronico = db.Column(db.String(50))
    gabineteid = db.Column(db.Integer, db.ForeignKey('gabinete.gabineteid'))
    gabinete = db.relationship('Gabinete', back_populates='abogados')

class Procurador(db.Model):
    __tablename__ = 'procurador'
    procuradorID = db.Column(db.Integer, primary_key=True)
    DNI = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(15))
    correoElectronico = db.Column(db.String(50))

class Asunto(db.Model):
    __tablename__ = 'asunto'
    expedienteid = db.Column(db.Integer, primary_key=True)
    clienteid = db.Column(db.Integer, db.ForeignKey('cliente.clienteid'))
    descripcion =db. Column(db.String)
    fechainicio = db.Column(db.Date)
    fechafin = db.Column(db.Date)
    estado = db.Column(db.String(50))
    cliente = db.relationship('Cliente')

class Audiencia(db.Model):
    __tablename__ = 'audiencia'
    audienciaid = db.Column(db.Integer, primary_key=True)
    asuntoid = db.Column(db.Integer, db.ForeignKey('asunto.expedienteid'))
    fecha = db.Column(db.Date)
    abogadoid = db.Column(db.Integer, db.ForeignKey('abogado.abogadoid'))
    incidencias = db.Column(db.String)
    asunto = db.relationship('Asunto')
    abogado = db.relationship('Abogado')

# Tabla de relación Many-to-Many entre Asunto y Procurador
asunto_procurador = db.Table('asunto_procurador', Base.metadata,
    db.Column('asuntoid', db.Integer, db.ForeignKey('asunto.expedienteid')),
    db.Column('procuradorid', db.Integer, db.ForeignKey('procurador.procuradorid'))
)
