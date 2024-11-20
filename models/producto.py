from flask_sqlalchemy import SQLAlchemy
from db import db
from models.ingrediente import Ingrediente
from funciones import *

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column("nombre", db.String(45), nullable = False)
    precio = db.Column("precio", db.Integer, nullable = False)
    id_ingrediente1 = db.Column(db.Integer,db.ForeignKey('ingredientes.id'), nullable=False)
    id_ingrediente2 = db.Column(db.Integer,db.ForeignKey('ingredientes.id'), nullable=False)
    id_ingrediente3 = db.Column(db.Integer,db.ForeignKey('ingredientes.id'), nullable=False)
    tipo = db.Column("tipo", db.String(15), nullable = False)
    # ingredientes = None