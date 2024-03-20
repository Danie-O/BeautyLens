from app import db, ma, login
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
    reviews = db.relationship('Review', backref='reviewer', lazy='dynamic', cascade='all, delete')
    joined_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64), index=True)
    brand = db.Column(db.String(120), index=True)
    name = db.Column(db.String(120), index=True)
    hex_color = db.Column(db.String(16), index=True)
    skintone = db.Column(db.String(120), index=True)
    product_url = db.Column(db.String(120))
    price = db.Column(db.Integer, index=True)
    skintype = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<Product {}>'.format(self.name)


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'brand', 'name', 'price')


product_schema = ProductSchema()
products_schema = ProductSchema(many = True)

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
    
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__():
        return '<Review {}'.format(self.review)