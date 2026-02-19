from wtforms import Form, StringField,IntegerField,EmailField,PasswordField,SubmitField, validators



class UserForm(Form):
    nombre=StringField("Nombre")
    apaterno=StringField("Apellido Paterno")
    amaterno=StringField("Apellido Materno")
    edad=IntegerField("Edad")
    correo=EmailField("Email")
    matricula=IntegerField("Matricula")

