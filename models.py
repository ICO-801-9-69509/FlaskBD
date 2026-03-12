from flask_sqlalchemy import SQLAlchemy
import datetime

db=SQLAlchemy()

class Alumnos(db.Model):
    __tablename__='alumnos'
    matricula=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50),nullable=False)
    apaterno=db.Column(db.String(50),nullable=False)
    amaterno=db.Column(db.String(50),nullable=False)
    edad=db.Column(db.Integer,nullable=False)
    correo=db.Column(db.String(50),nullable=False)

    def __init__(self,matricula,nombre,apaterno,amaterno,edad,correo):
        self.matricula=matricula
        self.nombre=nombre
        self.apaterno=apaterno
        self.amaterno=amaterno
        self.edad=edad
        self.correo=correo

class Maestros(db.Model):
    __tablename__='maestros'
    clave=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50),nullable=False)
    apaterno=db.Column(db.String(50),nullable=False)
    amaterno=db.Column(db.String(50),nullable=False)
    edad=db.Column(db.Integer,nullable=False)
    correo=db.Column(db.String(50),nullable=False)
    especialidad=db.Column(db.String(50),nullable=False)
    #cursos=db.Column(db.Integer,nullable=False)

    def __init__(self,clave,nombre,apaterno,amaterno,edad,correo,especialidad):#,cursos):
        self.clave=clave
        self.nombre=nombre
        self.apaterno=apaterno
        self.amaterno=amaterno
        self.edad=edad
        self.correo=correo
        self.especialidad=especialidad
        #self.cursos=cursos