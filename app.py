from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True) 
@app.route('/index')
def hello_world():
    name = "fabito"
    return render_template('index.html', name=name)


#LOGICA PARA INICIAR SESION O REGISTRARSE :D
@app.route('/')
def Login():
    return render_template('auth/Login.html')
@app.route('/CrearCuenta')
def Registrar():
    return render_template('auth/Registro.html')




