import flask
from forms import UserForm
from flask_wtf.csrf import CSRFProtect
from models import db,alumnos
from config import DevelopmentConfig

app=flask.Flask("__main__")
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf=CSRFProtect(app)

@app.route("/")
def main():
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
    app.run(debug=True,port=5001)
