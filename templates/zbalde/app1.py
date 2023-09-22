from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/admin')
def admin():
    return render_template('sitio/admin.html')

@app.route('/evaluador')
def evaluador():
    return render_template('sitio/evaluador.html')

@app.route('/paciente')
def paciente():
    return render_template('sitio/paciente.html')

@app.route('/juegos')
def juegos():
    return render_template('sitio/juegos.html')


@app.route('/admin')
def admin_index():
    return render_template('admin/admin.html')

@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/evaluador')
def evaluadora():
    return render_template('admin/evaluadora.html')

@app.route('/paciente')
def pacientea():
    return render_template('admin/pacientea.html')

@app.route('/juegosa')
def juegosa():
    return render_template('admin/juegosa.html')

@app.route('/informes')
def informes():
    return render_template('admin/informes.html')

@app.route('/historiaclinica')
def historiaclinica():
    return render_template('admin/historiaclinica.html')

@app.route('/archivo')
def archivo():
    return render_template('admin/archivo.html')


if __name__ == '__main__':
    app.run(debug=True) 

