from flask_sqlalchemy import SQLAlchemy
from db import db
from abc import ABC, abstractmethod

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column("nombre", db.String(45), nullable = False)
    precio = db.Column("precio", db.Integer, nullable = False)
    calorias = db.Column("calorias", db.NUMERIC(5,2), nullable = False)
    vegetariano = db.Column("vegetariano", db.BOOLEAN, nullable = False)
    inventario = db.Column("inventario", db.NUMERIC(5,2), nullable = False)
    tipo = db.Column("tipo", db.String(15), nullable = False)
    sabor = db.Column("sabor", db.String(45), nullable = False)