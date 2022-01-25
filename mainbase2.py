from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mainbase.db'
db = SQLAlchemy(app)


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    name = db.Column(db.String(80), nullable=True)
    categor = db.relationship('Categories', backref=db.backref('categories', lazy=False))
    
    
class Proisvoditeli(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    name = db.Column(db.String(80), nullable=True)
    proisvodit = db.relationship('Proisvoditeli', backref=db.backref('proisvoditeli', lazy=False))

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    name = db.Column(db.String(80), nullable=True)
    proisvoditeli_id = db.Column(db.Integer, db.ForeignKey('proisvoditeli.id'), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    produc = db.relationship('Products', backref=db.backref('products', lazy=False))


class Price_change(db.Model):
    i = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=True)
    date_price_change = db.Column(db.Float, nullable=True)
    new_price = db.Column(db.Integer, nullable=True)
    

class Stores(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    name = db.Column(db.String(80), nullable=True)
    stor = db.relationship('Stores', backref=db.backref('stores', lazy=False))
    

class Deliveries(db.Model):
    i = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=True)
    delivery_date = db.Column(db.Integer, nullable=True)
    product_count = db.Column(db.Integer, nullable=True)

    
class Klienti(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    name = db.Column(db.String(80), nullable=True)
    klien = db.relationship('Klienti', backref=db.backref('klienti', lazy=False))


class Pocupki(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    klienti_id = db.Column(db.Integer, db.ForeignKey('klienti.id'), nullable=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=True)
    pocupki_date = db.Column(db.Integer, nullable=True)
    pocup = db.relationship('Pocupki', backref=db.backref('pocupki', lazy=False))


class Pocupki_items(db.Model):
    i = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    pocupki_id = db.Column(db.Integer, db.ForeignKey('pocupki.id'), nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=True)
    product_count = db.Column(db.Integer, nullable=True)
    product_price = db.Column(db.Float, nullable=True)
    


db.create_all()