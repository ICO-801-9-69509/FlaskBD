from wtforms.validators import email

import flask
from forms import TeacherForm, UserForm
from flask_wtf.csrf import CSRFProtect
from models import db, Alumno, Maestro, Inscripcion, Curso
from config import DevelopmentConfig
from flask_migrate import Migrate

app=flask.Flask("__main__")
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate=Migrate(app,db) 
#flask db init para crear migraciones solo se corre una vez
#flask db migrate -m "mensaje" para subir los cambios
#flask db upgrade realiza los cambios
csrf=CSRFProtect(app)

@app.route("/index")
@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
    #select * from alumnos
    alumno=Alumno.query.all()
    return flask.render_template("alumnos.html",alumno=alumno)

@app.route('/alumnos/nuevo',methods=["GET","POST"])
def nuevo_alumno():
    create_alumno =UserForm(flask.request.form)
    
    if flask.request.method=="POST":
        alum=Alumno(
            matricula=create_alumno.matricula.data,
            nombre=create_alumno.nombre.data,
            amaterno=create_alumno.amaterno.data,
            apaterno=create_alumno.apaterno.data,
            edad=create_alumno.edad.data,
            correo=create_alumno.correo.data)
        db.session.add(alum)
        db.session.commit()
        return flask.redirect("alumnos.html")
    return flask.render_template("nuevo_alumno.html",form=create_alumno)


@app.route("/maestros",methods=["GET","POST"])
def maestros():
    create_maestro=TeacherForm(flask.request.form)
    maestro=Maestro.query.all()
    return flask.render_template("maestros.html",form=create_maestro,maestro=maestro)

@app.route("/usuarios",methods=["GET","POST"])
def usuario():
    mat=0
    nom=''
    apa=''
    ama=''
    edad=0
    email=''
    usuarios_clas=UserForm(flask.request.form)
    if flask.request.method=='POST':
        mat=usuarios_clas.matricula.data
        nom=usuarios_clas.nombre.data
        apa=usuarios_clas.apaterno.data
        ama=usuarios_clas.amaterno.data
        edad=usuarios_clas.edad.data
        email=usuarios_clas.correo.data
    
    return flask.render_template('usuarios.html',form=usuarios_clas,mat=mat,
                           nom=nom,apa=apa,ama=ama,edad=edad,email=email)
    
if __name__=="__main__":
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
