from flask import Flask
from .models import db
from .routes import crud

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:eegc@localhost/socioslealesSA'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'tu_clave_secreta'
    db.init_app(app)
    app.register_blueprint(crud)
    return app

