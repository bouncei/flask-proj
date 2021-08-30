from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Secret key
    app.config['SECRET_KEY'] = 'joshua inyang'

    # Datebase
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/hp/Documents/Python/Projects/test/databases/posts.db'


    app.config['SQLALCHEMY_BINDS'] = {
        'users' : 'sqlite:////Users/hp/Documents/Python/Projects/test/databases/users.db'
    }

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

     

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
