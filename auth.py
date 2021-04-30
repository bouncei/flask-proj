from .config import *
from flask_login import login_user, login_required, logout_user, current_user
from models import BlogPost, db, User
auth = Blueprint('auth', __name__)