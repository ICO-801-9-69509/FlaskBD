from wtforms.validators import email


import flask
from forms import UserForm,Filtro
from flask_wtf.csrf import CSRFProtect
from models import db,Maestro,Alumno,Curso,Inscripcion
from config import DevelopmentConfig
from flask_migrate import Migrate
from Maestros.routes import maestros_bp
from Alumnos.routes import alumnos_bp
from Cursos.routes import cursos_bp


app=flask.Flask("__main__")
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros_bp)
app.register_blueprint(alumnos_bp)
app.register_blueprint(cursos_bp)
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

@app.route("/consultas/impartidos",methods=["GET","POST"])
def impartidos():
    #dropdown de maestros
    drop=Filtro("Maestros",flask.request.args)
    drop.drop.choices=[(a.clave, f"{a.nombre} {a.apaterno}") for a in Maestro.query.all()]
    id=flask.request.args.get('drop')
    cursos=[]
    if id:
        cursos=Curso.query.filter_by(id_maestro=id).all()
    
    return flask.render_template("impartidos_maestro.html",form=drop,cursos=cursos)

@app.route("/consultas/inscrito",methods=["GET","POST"])
def inscripciones():
    #dropdown de alumnos
    drop=Filtro("Alumnos",flask.request.args)
    drop.drop.choices=[(a.matricula, f"{a.nombre} {a.apaterno}") for a in Alumno.query.all()]
    id=flask.request.args.get('drop')
    cursos=[]
    if id:
        # Get the alumno and their enrolled courses using the relationship
        alumno = Alumno.query.get(id)
        if alumno:
            cursos = alumno.cursos

    return flask.render_template("inscripciones_alumno.html", cursos=cursos, form=drop)
    

@app.route("/consultas/matriculados") 
def matriculados():
    #dropdown de cursos
    drop=Filtro("Cursos",flask.request.args)
    drop.drop.choices=[(a.id_curso, f"{a.nombre}") for a in Curso.query.all()]
    id=flask.request.args.get('drop')
    inscripciones=[]
    if id:
        inscripciones = Inscripcion.query.filter_by(id_curso=id).all()
    return flask.render_template("alumnos_inscritos.html",form=drop, alumnos=inscripciones)

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


