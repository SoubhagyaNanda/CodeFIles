from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

db = SQLAlchemy()

def create_app():
    app= Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///./blueprints.db'
    db.init_app(app)

    migrate=Migrate(app,db)
    return app
