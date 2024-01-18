from app import app, db
from models import User, Product, Recommendation, BlogPost, Comment

with app.app_context():
    db.create_all()