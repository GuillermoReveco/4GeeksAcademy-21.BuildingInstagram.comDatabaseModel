import os
import sys
from sqlalchemy import Column, ForeignKey, Table, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

followers = Table(
    "followers",
    Base.metadata,
    Column("usuario_id", ForeignKey("usuario.id")),
    Column("follower_id", ForeignKey("usuario.id")),
)

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellidos = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    children = relationship("followers")

    def serialize(self):
        return{
            "id" : id.self,
            "nombre" : nombre.self,
            "apellidos" : apellidos.self,
            "email" : email.self,
            "password" : password.self,
            "followers": self.followers,
        }

class Posteo(Base):
    __tablename__ = 'posteo'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    mensaje = Column(String(250))
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship(Usuario)

    def serialize(self):
        return{
            "id" : id.self,
            "mensaje" : mensaje.self,
            "usuario_id" : usuario_id.self,
        }

class Comentario(Base):
    __tablename__ = 'comentario'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comentario_txt = Column(String(250))
    autor_id = Column(Integer, ForeignKey("usuario.id"))
    posteo_id = Column(Integer, ForeignKey("posteo.id"))
    usuario = relationship(Usuario)
    posteo = relationship(Posteo)

    def serialize(self):
        return{
            "id" : id.self,
            "comentario_txt" : comentario_txt.self,
            "autor_id" : autor_id.self,
            "posteo_id" : posteo_id.self,
        }

class Pagina(Base):
    __tablename__ = 'pagina'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    tipo = Column(String(250))
    url = Column(String(250))
    posteo_id = Column(Integer, ForeignKey("posteo.id"))
    posteo = relationship(Posteo)

    def serialize(self):
        return{
            "id" : id.self,
            "tipo" : comentario_txt.self,
            "url" : comentario_txt.self,
            "posteo_id" : posteo_id.self,
        }


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')