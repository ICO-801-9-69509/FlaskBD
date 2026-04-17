import flask
from . import alumnos_bp
from forms import UserForm
from models import Inscripcion, db, Alumno

#flask --app Alumnos run
#python -m Alumnos.__init__


@alumnos_bp.route("/alumnos",methods=["GET",])
def alumnos():
    #select * from alumnos
    alumno=Alumno.query.all()
    return flask.render_template("alumnos.html",alumno=alumno)

@alumnos_bp.route('/alumnos/nuevo',methods=["GET","POST"])
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
        return flask.redirect("/alumnos")
    return flask.render_template("nuevo_alumno.html",form=create_alumno)

@alumnos_bp.route('/alumnos/detalles/<int:id>')
def detalles_alumno(id:int):
    alumno=Alumno.query.get_or_404(id)
    return flask.render_template("detalles_alumno.html",alumno=alumno)
    

@alumnos_bp.route("/alumnos/<int:id>",methods=["GET","POST"])
def actualizar_alumno(id:int):
    alumno=Alumno.query.get_or_404(id)
    update_alumno=UserForm(flask.request.form)
    if flask.request.method=="POST" and update_alumno.validate():
        alumno.nombre = update_alumno.nombre.data
        alumno.apaterno = update_alumno.apaterno.data
        alumno.amaterno = update_alumno.amaterno.data
        alumno.correo = update_alumno.correo.data
        alumno.edad = update_alumno.edad.data
        db.session.commit() 
        return flask.redirect("/alumnos")
    return flask.render_template("actualizar_alumno.html",form=update_alumno,alumno=alumno)

@alumnos_bp.route("/alumnos/eliminar/<int:id>",methods=["GET","POST"])
def eliminar(id:int):
    alumno=Alumno.query.get_or_404(id)
    if flask.request.method=="POST":
        Inscripcion.query.filter_by(id_alumno=id).delete() #elimianr inscripciones del alumno
        db.session.delete(alumno)
        db.session.commit()
        return flask.redirect("/alumnos")
    return flask.render_template("eliminar_alumno.html",alumno=alumno.to_dict())