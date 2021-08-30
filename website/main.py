from flask import Blueprint, render_template, request, redirect, url_for
from .models import BlogPost, User
from . import db
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    
    return render_template('hello.html', user=current_user)


# Creating a New BlogPost and adding it to the database
@main.route('/posts', methods=['GET', 'POST'])
@login_required
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
@main.route('/posts/delete/<int:id>')
@login_required
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

 
# Editing a BlogPost
@main.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
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
@main.route('/posts/new_post', methods=['GET', 'POST'])
@login_required
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
