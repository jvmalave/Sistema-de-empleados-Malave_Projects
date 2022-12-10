
from flask import Flask
from flask import render_template,request,redirect,url_for, flash
from flaskext.mysql import MySQL
from flask import send_from_directory

from datetime import datetime
import os


app=Flask(__name__)
app.secret_key="Malave"

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema'
mysql.init_app(app)

CARPETA= os.path.join('uploads')
app.config['CARPETA']=CARPETA

@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'],nombreFoto)

@app.route('/')
def index():

    sql="SELECT * FROM `empleados`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
   
    empleados=cursor.fetchall()
    print(empleados)

    conn.commit()
    return render_template('empleados/index.html' , empleados=empleados )

@app.route('/destroy/<int:id>')
def destroy(id):
    conn=mysql.connect()
    cursor=conn.cursor()

    cursor.execute("SELECT foto_empleado FROM empleados WHERE id_empleado=%s",id)
    fila=cursor.fetchall()

    os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))

    cursor.execute("DELETE FROM empleados WHERE id_empleado=%s",(id))
    conn.commit()
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):

    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM empleados WHERE id_empleado=%s",(id))
    empleados=cursor.fetchall()
    conn.commit()
    
    return render_template('empleados/edit.html' , empleados=empleados)

@app.route('/update', methods=['POST'])
def update():
    _nombre=request.form['txtNombre']
    _apellido=request.form['txtApellido']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']
    _fecha=request.form['txtFecha']
    id=request.form['txtId'] 

    sql="UPDATE empleados SET nombre_empleado=%s, apellido_empleado=%s, correo_empleado=%s, fecha_nacimiento=%s WHERE id_empleado=%s;"
    
    datos=(_nombre,_apellido,_correo,_fecha,id)
    
    conn=mysql.connect()
    cursor=conn.cursor()

    now= datetime.now()
    tiempo=now.strftime("%Y%H%M%S")

    if _foto.filename!='':

        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/" +nuevoNombreFoto)

        cursor.execute("SELECT foto_empleado FROM empleados WHERE id_empleado=%s",id)
        fila=cursor.fetchall()

        os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
        cursor.execute("UPDATE empleados SET foto_empleado=%s WHERE id_empleado=%s",(nuevoNombreFoto,id))
        conn.commit()

    cursor.execute(sql,datos)

    conn.commit()

    return redirect('/')

@app.route('/create')
def create():

   return render_template('empleados/create.html')


@app.route('/store', methods=['POST'])
def storage():
    _nombre=request.form['txtNombre']
    _apellido=request.form['txtApellido']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']
    _fecha=request.form['txtFecha']

    if _nombre=='' or _apellido=='' or _correo=='' or _foto=='' or _fecha=='':
        flash('Recuerda llenar todos los datos de los campos')
        return redirect(url_for('create'))

    now= datetime.now()
    tiempo=now.strftime("%Y%H%M%S")

    if _foto.filename!='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/" +nuevoNombreFoto)

    sql="INSERT INTO `empleados` (`id_empleado`, `nombre_empleado`, `apellido_empleado`, `correo_empleado`, `foto_empleado`, `fecha_nacimiento`) VALUES (NULL, %s, %s, %s, %s, %s);"
    
    datos=(_nombre,_apellido,_correo,nuevoNombreFoto,_fecha)
    
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect ('/')


if __name__=='__main__':
    app.run(debug=True)
    
