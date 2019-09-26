from flask import render_template, request, redirect, url_for,abort
from . import main
from .forms import PostForm,UpdateProfile
from app.models import User,PhotoProfile,Post
from flask_login import login_required,current_user
from .. import db,photos

@main.route('/')
def home():
    #all_posts = Post.query.all()
    #print(all_posts)
    return render_template('base.html')

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():

        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/pitch',methods = ['GET','POST'])
@login_required
def post_pitch():
    uname = current_user.username
    form = PostForm()
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    if form.validate_on_submit:
        title = form.title.data
        blog = form.blog.data
        #category = form.category.data
        post = Post.query.filter_by(title = title ).first()
        if post == None:
            new_post = Post(title = title , blog = blog,  )
            db.session.add(new_post)
            db.session.commit()

    #return redirect(url_for('.profile',uname=user.username))

    return render_template('postblog.html',form =form)    

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        print(request.files['photo'])
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        #user_photo = PhotoProfile(pic_path = path,user = user)
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname,id_user=current_user.id))