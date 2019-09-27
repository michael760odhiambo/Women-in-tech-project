class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    post = db.Column(db.String(255))
    users = db.relationship('User', backref='post', lazy='dynamic')
    #comments = db.relationship('Comment', backref='article', lazy=True)

    def __repr__(self):
        return f"Post{self.blog}"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
