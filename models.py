from flask_sqlalchemy import SQLAlchemy
import datetime

db=SQLAlchemy()

class Alumno(db.Model):
    __tablename__='alumnos'
    matricula=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(150),nullable=False)
    apaterno=db.Column(db.String(50),nullable=False)
    amaterno=db.Column(db.String(100),nullable=False)
    edad=db.Column(db.Integer,nullable=False)
    correo=db.Column(db.String(100),nullable=True)
    created_date=db.Column(db.DateTime,default=datetime.datetime.now)
    
    cursos= db.relationship("Curso",secondary="inscripciones",back_populates="alumnos")

    def __init__(self,matricula,nombre,apaterno,amaterno,edad,correo,created_date):
        self.matricula=matricula
        self.nombre=nombre
        self.apaterno=apaterno
        self.amaterno=amaterno
        self.edad=edad
        self.correo=correo
        self.created_date=created_date


class Curso(db.Model):
    __tablename__="cursos"
    id_curso=db.Column(db.Integer,primary_key=True, autoincrement=True)
    nombre=db.Column(db.String(40),nullable=False)
    descripcion=db.Column(db.String(100),nullable=False)
    id_maestro=db.Column(db.Integer,db.ForeignKey("maestros.clave"),nullable=False)
    maestros=db.relationship("Maestro",back_populates="cursos")
    alumnos= db.relationship("Alumno",secondary="inscripciones", back_populates="cursos")
    #db.relationship("NombreDeLaClaseRelacionada",secondary="nombre_tabla_intermedia",back_populates="nombre_en_la_otra_clase")


    def __init__(self,id_curso,nombre,descripcion,id_maestro):
        self.id_curso=id_curso
        self.nombre=nombre
        self.descripcion=descripcion
        self.id_maestro=id_maestro

class Inscripcion(db.Model):
    __tablename__="inscripciones"
    id_inscripcion=db.Column(db.Integer,primary_key=True, autoincrement=True)
    id_alumno=db.Column(db.Integer, db.ForeignKey("alumnos.matricula"),nullable=False)
    id_curso=db.Column(db.Integer, db.ForeignKey("cursos.id_curso"),nullable=False)
    fecha_inscripcion=db.Column(db.DateTime,default=datetime.datetime.now)

    __table_args__=(
        db.UniqueConstraint("id_alumno","id_curso",name="uq_alumno_curso")
    )
    

    def __init__(self, id_alumno, id_curso, fecha_inscripcion=None):
        self.id_alumno = id_alumno
        self.id_curso = id_curso
        if fecha_inscripcion:
            self.fecha_inscripcion = fecha_inscripcion


class Maestro(db.Model):
    __tablename__='maestros'
    clave=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50),nullable=False)
    apaterno=db.Column(db.String(50),nullable=False)
    amaterno=db.Column(db.String(50),nullable=False)
    edad=db.Column(db.Integer,nullable=False)
    correo=db.Column(db.String(50),nullable=False)
    especialidad=db.Column(db.String(50),nullable=False)
    
    cursos=db.relationship("Curso",back_populates="maestros")
    #cursos=db.Column(db.Integer,nullable=False)

    def __init__(self,clave,nombre,apaterno,amaterno,edad,correo,especialidad):#,cursos):
        self.clave=clave
        self.nombre=nombre
        self.apaterno=apaterno
        self.amaterno=amaterno
        self.edad=edad
        self.correo=correo
        self.especialidad=especialidad
        #self.cursos=cursosursos