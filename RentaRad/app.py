from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
import csv
from funciones import funcionesmecas

bicicleta=funcionesmecas.read_csv_to_dict('baikas.csv')

app = Flask(__name__)
app.config['SECRET_KEY'] = '1111111'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/perfil')
def perfil():
    # Aquí debes incluir el código para obtener y mostrar las bicicletas en renta del usuario
    return render_template('perfil.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('rent'))
    else:
        return render_template('rent.html')

@app.route('/rentar', methods=['POST'])
def rentar():
    nombre = request.form['nombre']
    fecha = request.form['fecha']
    tiempo = request.form['tiempo']
    # procesa la renta de la bicicleta y muestra una página de confirmación
    return render_template('confirmacion.html', nombre=nombre, fecha=fecha, tiempo=tiempo)


@app.route('/rent')
@login_required
def rent():
    print(bicicleta)
    return render_template('rent.html',bicicletas=bicicleta)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



if __name__=='__main__':
    app.run(debug=True)
