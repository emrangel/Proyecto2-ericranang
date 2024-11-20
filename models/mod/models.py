from flask_sqlalchemy import SQLAlchemy
from db import db

class Ingrediente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    ingredientes = db.relationship('Ingrediente', secondary='producto_ingrediente')

class ProductoIngrediente(db.Model):
    __tablename__ = 'producto_ingrediente'
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), primary_key=True)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey('ingrediente.id'), primary_key=True)
