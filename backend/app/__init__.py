from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config
from .routers.ping_routes import ping_bp

#Inicializa SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) 
    db.init_app(app)
    CORS(app) # Habilita CORS para permitir llamadas del frontend

    # Registro de rutas (Blueprints)
    from .routers.patient_routes import patient_bp
    from .routers.ping_routes import ping_bp
    app.register_blueprint(patient_bp, url_prefix='/api/patients')
    app.register_blueprint(ping_bp, url_prefix='/api')

    return app