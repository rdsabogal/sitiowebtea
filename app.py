import os
from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL
from datetime import datetime
from flask import send_from_directory


app=Flask(__name__)
mysql=MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sitio'
mysql.init_app(app)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/img/<imagen>')
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join('templates/sitio/img'),imagen)

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

    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `juegosa`")
    juegosa=cursor.fetchall()
    conexion.commit()
    print(juegosa)
    return render_template("admin/juegosa.html", juegosa=juegosa)

@app.route('/admin/juegosa/guardar',methods=['POST'])
def admin_juegosa_guardar():

    _nombre=request.form['txtNombre']
    _url=request.form['txtURL']
    _archivo=request.files['txtImagen']

    tiempo= datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')

    if _archivo.filename!="":
        nuevoNombre=horaActual+"_"+_archivo.filename
        _archivo.save("templates/sitio/img/"+nuevoNombre)


    sql="INSERT INTO `juegosa` (`id`, `nombre`, `imagen`, `url`) VALUES (NULL,%s,%s,%s);"
    datos=(_nombre,nuevoNombre,_url)
    
    conexion= mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()

    print(_nombre)
    print(_url)
    print(_archivo)
    
    return redirect('/admin/juegosa')

@app.route('/admin/juegosa/borrar', methods=['POST'])
def admin_juegosa_borrar():
    _id=request.form['txtID']
    print(_id)

    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `juegosa` WHERE id=%s",(_id))
    juegosa=cursor.fetchall()
    conexion.commit()
    print(juegosa)

    if os.path.exists("templates/sitio/img/"+str(juegosa[0][0])):
        os.unlink("templates/sitio/img/"+str(juegosa[0][0]))

    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM juegosa WHERE id=%s",(_id))
    conexion.commit()

    return redirect('/admin/juegosa')

    
if __name__ == '__main__':
    app.run(debug=True) 

