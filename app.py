from config import *
from flask import url_for, request, render_template, redirect, flash
from markupsafe import escape
from models import BlogPost, db
# from flask_login import login_user, login_required, logout_user, current_user

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Home route
@app.route('/')
def index():
    
    return render_template('hello.html')


# Creating a New BlogPost and adding it to the database
@app.route('/posts', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        # post_title = request.form['title']
        # post_content = request.form['content']
        # post_author = request.form['author']

        # new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        # db.session.add(new_post)
        # db.session.commit()
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

# New BlogPost
@app.route('/posts/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']

        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')

    else:
        return render_template('new_post.html')


# Login 
@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Login User """
    # session.clear()



    return render_template('login.html')


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Register User """

    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        surname = request.form.get('surname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #check for input errors
        if len(email) < 3:
            flash('Email error', category='error')
        
        elif firstname or surname < 4:
            flash('Name should be more than 3 charachers', category='error')

        elif password1 != password2:
            flash('Passwords don\'t match ', category='error')

        elif password1 < 7:
            flash('Password must be more than 6 charachers', category='error')


        else:
            flash('Account Created!', category='success')

    else:
        return render_template('register.html')







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




if __name__ == '__main__':
    app.run(port=5000,debug=True)