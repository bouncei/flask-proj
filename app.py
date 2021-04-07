from flask import Flask, url_for, request, render_template, redirect
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#You need to use following line [app Flask(__name__]
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post' + str(self.id)


all_posts = [
    {
        'title': 'Post A',
        'content': 'contents of Post A',
        'author': 'ALfred Emmanuel'
    },

    {
        'title': 'Post B',
        'content': 'contents of Post B'
    },

    {
        'title': 'Post C',
        'content': 'contents for Post C',
        'author': 'Bouncey Inyang'
    }

]


@app.route('/')
def index():
    return "Hello World with flask"


@app.route('/posts', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']

        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')

    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     # return 'User %s Welcome!' % escape(username)

#     return '{}\'s profile'.format(escape(username))









# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(escape(username))

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))


@app.route('/yo/<name>')
def how_far(name=None):
    return render_template('hello.html', name=name)







if __name__ == '__main__':
    app.run(port=5000,debug=True)