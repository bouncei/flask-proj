from config import *
from flask import url_for, request, render_template, redirect
from markupsafe import escape
from models import BlogPost, db





# Home route
@app.route('/')
def index():
    
    return render_template('hello.html')


# Creating a New BlogPost and adding it to the database
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


# Deleting a BlogPost
@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')


# Editing a BlogPost
@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = request.form['author']
        db.session.commit()

        return redirect('/posts')
        
    else:
        return render_template('edit.html', post=post)










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