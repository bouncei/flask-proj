from flask import Flask, url_for
from markupsafe import escape


#You need to use following line [app Flask(__name__]
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World with flask"


@app.route('/welcome')
def welcome():
    return "Welcome To My HomePage"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     # return 'User %s Welcome!' % escape(username)

#     return '{}\'s profile'.format(escape(username))

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id  is an integer 
    return 'Post {}'.format(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
     # show the subpath after /path/
    # return 'Subpath %s' % escape(subpath)

    return '{}\'s subpath'.format(escape(subpath))   





@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))



if __name__ == '__main__':
    app.run(port=5000,debug=True)