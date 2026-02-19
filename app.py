import flask
from forms import UserForm

app=flask.Flask("__main__")

@app.route("/")
def main():
    return flask.render_template("index.html")

@app.route("/usuarios",methods=["GET","POST"])
def usuario():
    form=UserForm(flask.request.form)
    if flask.request.method=="POST":
        nom=form.nombre.data
        ape=form.apaterno.data
        ama=form.amaterno.data
        mat=form.matricula.data
        email=form.correo.data
        return flask.render_template("usuarios.html",form=form,
                                 data={'nombre':nom,
                                       'apaterno':ape,
                                       'amaterno':ama,
                                       'matricula':mat,
                                       'correo':email})
    return flask.render_template("usuarios.html",form=form)

if __name__=="__main__":
    app.run(debug=True,port=5001)
