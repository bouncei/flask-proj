from flask import Flask, url_for, request, render_template
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





@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()

    else:
        show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


@app.route('/yo/<name>')
def how_far(name=None):
    return render_template('hello.html', name=name)


@app.route('/home')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(port=5000,debug=True)