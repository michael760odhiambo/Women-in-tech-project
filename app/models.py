from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    #user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),index=True,unique=True)
    blog_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)    

    def __repr__(self):
        return f"User{self.username}, '{self.email}'"



class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    blog = db.Column(db.String(255))
    users = db.relationship('User', backref='post', lazy='dynamic')
   # comments = db.relationship('Comment', backref='article', lazy=True)

    def __repr__(self):
        return f"Post{self.blog}"

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(100), nullable=False)
   # timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    blog_id = db.Column(db.Integer,db.ForeignKey('posts.id'))

    def __repr__(self):
        return f"Comment('{self.body}')" 

