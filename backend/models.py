from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    past_recommendations = db.relationship('Recommendation', backref='user', lazy='dynamic', cascade='all, delete, delete-orphan')
    # favorites = db.relationship('FavoriteProduct', backref='user', lazy='dynamic', cascade='all, delete, delete-orphan')
    comments = db.relationship('Comment', backref='author', lazy='dynamic', cascade='all, delete, delete-orphan')
    joined_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, index=True)
    category = db.Column(db.String(64), index=True)
    brand = db.Column(db.String(120), index=True)
    skintone = db.Column(db.String(120), index=True)
    skintype = db.Column(db.String(120), index=True)
    hex_color = db.Column(db.String(16), index=True)
    product_url = db.Column(db.String(120), unique=True)
    price = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Product {}>'.format(self.name)


class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(128))
    product_category = db.Column(db.String(120), index=True)
    skintone = db.Column(db.String(120), index=True)
    skintype = db.Column(db.String(120), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# class FavoriteProduct(db.Model):
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     pass


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    author = db.Column(db.String(120), index=True)
    content = db.Column(db.String(1024))
    comments = db.relationship('Comment', backref='blogpost', lazy='dynamic', cascade='all, delete, delete-orphan')
    posted_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    last_updated = db.Column(db.DateTime(), index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<BlogPost {}>'.format(self.title)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(256))
    posted_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    blogpost_id = db.Column(db.Integer, db.ForeignKey('blog_post.id'))

    def __repr__(self):
        return '<BlogPost {}>'.format(self.title)
    
