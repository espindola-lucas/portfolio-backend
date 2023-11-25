from flask import Flask, render_template, request
from flask_socketio import SocketIO
from db import Session, engine
from models import User

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

session = Session()

@app.route('/', methods=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('name') and request.form.get('password'):
            name = request.form.get('name')
            password = request.form.get('password')
            user = session.query(User).filter_by(username=name, password=password).first()
            if user:
                return render_template('landingPage.html', user=user)
            else:
                return render_template('login.html', error='Contraseña o usuario incorrecto')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')  
        mail = request.form.get('email')  
        password = request.form.get('password')  

        with engine.connect() as con:
            new_user = User(username=name, email=mail, password=password)
            session.add(new_user)
            session.commit()
            return render_template('login.html')

    return render_template('signup.html')

@app.route('/landingPage')
def landingPage():
    return render_template('landingPage.html')

# TypeError: signup() missing 1 required positional argument: 'dataForm'
# @socketio.on('get_pokemon_id')
# def get_pokemon_id(pokemon_name):
#     url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
#     response = requests.get(url)

#     if response.status_code == 200:
#         pokemon_data = response.json()
#         pokemon_id = pokemon_data['id']
#         socketio.emit('pokemon_id', pokemon_id)
#     else:
#         socketio.emit('pokemon_id', f'Error: {response.status_code}')



if __name__ == '__main__':
    app.run(debug=True)
