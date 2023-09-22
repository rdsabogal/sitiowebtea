from flask import Flask
from flask import render_template, request, redirect

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')
@app.route('/admin/')
def admin():
    return render_template('admin/index.html')

@app.route('/evaluador')
def evaluador():
    return render_template('sitio/evaluador.html')

@app.route('/paciente')
def paciente():
    return render_template('sitio/paciente.html')

@app.route('/juegos')
def juegos():
    return render_template('sitio/juegos.html')


@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admin/libros')
def admin_libros():
    return render_template('admin/libros.html')

@app.route('/admin/evaluadora')
def admin_evaluadora():
    return render_template('admin/evaluadora.html')

@app.route('/admin/pacientea')
def admin_pacientea():
    return render_template('admin/pacientea.html')

@app.route('/admin/informes')
def admin_informes():
    return render_template('admin/informes.html')

@app.route('/admin/juegosa')
def admin_juegosa():
    return render_template('admin/juegosa.html')

@app.route('/admin/juegosa/guardar',methods=['POST'])
def admin_juegosa_guardar():
    _nombre=request.form['txtNombre']
    _url=request.form['txtURL']
    _archivo=request.files['txtImagen']


    print(_nombre)
    print(_url)
    print(_archivo)
    
    return redirect('/admin/juegosa')

    
if __name__ == '__main__':
    app.run(debug=True) 

