from . import db
from flask_login import UserMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


# Ensure templates are auto-reloaded
# app.config["TEMPLATES_AUTO_RELOAD"] = False

# app = Flask(__name__)

# db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/hp/Documents/Python/Projects/test/databases/posts.db'


# app.config['SQLALCHEMY_BINDS'] = {
#     'users' : 'sqlite:////Users/hp/Documents/Python/Projects/test/databases/users.db'
# }






# Blog Post Model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))     #A foriegn key column refrencing to the user id
    
    def __repr__(self): 
        return 'Blog post' + str(self.id)


class User(db.Model, UserMixin):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    # blogs = db.relationship('BlogPost')
    

