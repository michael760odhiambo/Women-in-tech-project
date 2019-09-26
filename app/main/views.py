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

@main.route('/motive')
def motive():
    return"""
    <div class="container-fluid" style="background-color:rgb(219, 168, 219) " text-align='center'>
    <dive class="row">
    
    <h1 style="background-color:rgb(219, 168, 219) " text-align='center'>Hello welcome to women in tech world motivations!</h1>

    <iframe src="https://www.youtube.com/embed/NkL5_IA-ZiA" width="440" height="200" frameborder="0" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/fOJ-KKtzDXI" width="440" height="200" frameborder="0" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/WBdNfOJ5vMY" width="440" height="200" frameborder="0" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/XzQjpLB350s" width="440" height="200" frameborder="0" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/kvefEAtrla0" width="440" height="200" frameborder="0" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/8sMOSMKNYKY" width="440" height="200" frameborder="0" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/8VZTtRX4HIk" width="440" height="200" frameborder="0" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/KHq_EDi2PE8" width="440" height="200" frameborder="0" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/BYP5NZVqB50" width="440" height="200" frameborder="0" allowfullscreen></iframe>

    </dive>
</div>
"""