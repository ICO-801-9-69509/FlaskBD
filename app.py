import flask
from forms import UserForm

app=flask.Flask("__main__")

@app.route("/")
def main():
    return flask.render_template("index.html")

@app.route("/usuarios")
def usuarios():
    form=UserForm()
    return flask.render_template("usuarios.html",form=form)

if __name__=="__main__":
    app.run(debug=True,port=5001)
