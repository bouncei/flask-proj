from config import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime


# Ensure templates are auto-reloaded

# Secret key
app.config['SECRET_KEY'] = 'joshua inyang'

# Datebase
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
# app.config["TEMPLATES_AUTO_RELOAD"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'



# app.config['SQLALCHEMY_BINDS'] = {
#     'users' : 'sqlite///users.db',
# }

db = SQLAlchemy(app)

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
    # __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    # blogs = db.relationship('BlogPost')
    

