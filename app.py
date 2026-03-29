from wtforms.validators import email


import flask
from forms import TeacherForm, UserForm
from flask_wtf.csrf import CSRFProtect
from models import db, Alumno, Maestro, Inscripcion, Curso
from config import DevelopmentConfig
from flask_migrate import Migrate
from Maestros.routes import maestros_bp
from Alumnos.routes import alumnos_bp


app=flask.Flask("__main__")
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros_bp)
app.register_blueprint(alumnos_bp)
db.init_app(app)
migrate=Migrate(app,db) 
#flask db init para crear migraciones solo se corre una vez
#flask db migrate -m "mensaje" para subir los cambios
#flask db upgrade realiza los cambios

#blueprint
csrf=CSRFProtect(app)

@app.route("/index")
@app.route("/")
def index():
    return flask.render_template("index.html")    

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


