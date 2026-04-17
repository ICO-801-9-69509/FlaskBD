from wtforms import Form, StringField,IntegerField,EmailField,PasswordField,SubmitField, validators, SelectField, DateField

from models import Alumno, Maestro, Curso, Inscripcion

class UserForm(Form):
    nombre=StringField("Nombre")
    apaterno=StringField("Apellido Paterno")
    amaterno=StringField("Apellido Materno")
    edad=IntegerField("Edad")
    correo=EmailField("Email")
    matricula=IntegerField("Matricula")

class TeacherForm(Form):
    nombre=StringField("Nombre")
    apaterno=StringField("Apellido Paterno")
    amaterno=StringField("Apellido Materno")
    edad=IntegerField("Edad")
    correo=EmailField("Email")
    clave=IntegerField("clave")
    especialidad=StringField("Especialidad")
    #cursos

class CourseForm(Form):
    nombre=StringField("Nombre")
    descripcion=StringField("Descripcion")
    maestro=SelectField("Maestro", coerce=int)

class InscriptionForm(Form):
    curso=SelectField("Curso",coerce=int)
    alumno=SelectField("Alumno",coerce=int)
    fecha=DateField('fecha (opcional)', format='%Y-%m-%d')


class Filtro(Form):
    drop = SelectField(0, coerce=int)
    def __init__(self, name, *args, **kwargs):
        super(Filtro, self).__init__(*args, **kwargs)
        self.drop.label.text = name

    
    