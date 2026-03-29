import flask
from . import maestros_bp
from forms import TeacherForm
from models import db, Maestro

@maestros_bp.route("/maestros",methods=["GET","POST"])
def maestros():
    create_maestro=TeacherForm(flask.request.form)
    maestro=Maestro.query.all()
    return flask.render_template("maestros.html",form=create_maestro,maestro=maestro)

@maestros_bp.route("/maestros/nuevo",methods=["GET","POST"])
def nuevo_maestro():
    maestro=TeacherForm(flask.request.form)
    if flask.request.method=="POST":
        nuevo_maestro=Maestro(clave=maestro.clave.data,
        nombre=maestro.nombre.data,
        apaterno=maestro.apaterno.data,
        amaterno=maestro.amaterno.data,
        edad=maestro.edad.data,
        correo=maestro.correo.data,
        especialidad=maestro.especialidad.data)
        db.session.add(nuevo_maestro)
        db.session.commit()
        return flask.redirect("/maestros")

    return flask.render_template("nuevo_maestro.html",form=maestro)

@maestros_bp.route("/maestros/detalles/<int:id>")
def detalles_maestro(id:int):
    maestro=Maestro.query.get_or_404(id)
    return flask.render_template("detalles_maestro.html",maestro=maestro)

@maestros_bp.route('/maestros/<int:id>',methods=["GET","POST"])
def actualizar_maestro(id:int):
    form=TeacherForm(flask.request.form)
    maestro=Maestro.query.get_or_404(id)
    if flask.request.method=="POST":
        for field in form:
            setattr(maestro,field.name,field.data) if hasattr(maestro,field.name) and field.id not in ['clave', 'csrf_token', 'submit'] else None
        db.session.commit()
        return flask.redirect("/maestros")
    return flask.render_template("actualizar_maestro.html",maestro=maestro,form=form)

@maestros_bp.route("/maestros/eliminar/<int:id>",methods=["GET","POST"])
def eliminar_maestro(id:int):
    maestro=Maestro.query.get_or_404(id)
    if flask.request.method=="POST":
        db.session.delete(maestro)
        db.session.commit()
        return flask.redirect("/maestros")
    return flask.render_template("eliminar_maestro.html",maestro=maestro.to_dict())
