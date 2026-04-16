import flask
from . import cursos_bp
from forms import InscriptionForm,CourseForm
from models import db, Curso, Inscripcion, Maestro, Alumno

@cursos_bp.route("/cursos")
def listar_cursos():
    cursos=Curso.query.all()
    for curso in cursos:
        maestro=Maestro.query.get(curso.id_maestro)
    return flask.render_template("cursos.html",cursos=cursos,maestro=maestro)

@cursos_bp.route("/cursos/nuevo",methods=["GET","POST"])
def agregar_curso():
    form=CourseForm(flask.request.form)
    form.maestro.choices=[(m.clave,f"{m.nombre} {m.apaterno} {m.amaterno}")for m in Maestro.query.all()]
    if flask.request.method=="POST":
        nuevo_curso=Curso(nombre=form.nombre.data,descripcion=form.descripcion.data,id_maestro=form.maestro.data)
        db.session.add(nuevo_curso)
        db.session.commit()
        return flask.redirect("/cursos")
    return flask.render_template("nuevo_curso.html",form=form)

@cursos_bp.route("/cursos/detalles/<int:id>")
def detalles_curso(id):
    curso=Curso.query.get_or_404(id)
    maestro=Maestro.query.get(curso.id_maestro)
    return flask.render_template("detalles_curso.html",curso=curso,maestro=maestro)

@cursos_bp.route("/cursos/<int:id>",methods=["GET","POST"])#update curso
def actualizar_curso(id):
    curso=Curso.query.get_or_404(id)
    form=CourseForm(flask.request.form)
    form.maestro.choices=[(m.clave,f"{m.nombre} {m.apaterno} {m.amaterno}")for m in Maestro.query.all()]
    if flask.request.method=="POST":
        curso.nombre=form.nombre.data if form.nombre.data else curso.nombre
        curso.descripcion=form.descripcion.data if form.descripcion.data else curso.descripcion
        curso.id_maestro=form.maestro.data if form.maestro.data else curso.id_maestro
        db.session.commit()
        return flask.redirect("/cursos")
    return flask.render_template("actualizar_curso.html",form=form, curso=curso)


@cursos_bp.route("/cursos/eliminar/<int:id>",methods=["GET","POST"])
def eliminar_curso(id):
    curso=Curso.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()
    return flask.redirect("/cursos")

@cursos_bp.route("/cursos/inscripciones")
def listar_inscripciones():
    inscripciones=Inscripcion.query.all()
    return flask.render_template("inscripciones.html",inscripciones=inscripciones)

@cursos_bp.route("/cursos/inscripciones/nueva",methods=["GET","POST"])
def agregar_inscripcion():
    form=InscriptionForm(flask.request.form)
    form.curso.choices=[(c.id_curso,c.nombre) for c in Curso.query.all()]
    form.alumno.choices=[(a.matricula,f"{a.nombre} {a.apaterno} {a.amaterno}") for a in Alumno.query.all()]
    if flask.request.method=="POST":
        nueva=Inscripcion(id_alumno=form.alumno.data,id_curso=form.curso.data,fecha_inscripcion=form.fecha.data)
        db.session.add(nueva)
        db.session.commit()
        return flask.redirect("/cursos/inscripciones")
    return flask.render_template("nueva_inscripcion.html",form=form)

@cursos_bp.route("/cursos/eliminar",methods=["GET","POST"])
def eliminar_inscripcion():
    form=InscriptionForm(flask.request.form)
    form.curso.choices=[(c.id_curso,c.nombre) for c in Curso.query.all()]
    form.alumno.choices=[(a.matricula,f"{a.nombre} {a.apaterno} {a.amaterno}") for a in Alumno.query.all()]
    if flask.request.method=="POST":
        nueva=Inscripcion(id_alumno=form.alumno.data,id_curso=form.curso.data,fecha_inscripcion=form.fecha.data)
        db.session.add(nueva)
        db.session.commit()
        return flask.redirect("/cursos/inscripciones")
    return flask.render_template("nueva_inscripcion.html",form=form)

