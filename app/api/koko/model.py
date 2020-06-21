from app.extensions import db


class Store(db.Model):
    store_id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    customer_id = db.relationship("Customer",backref='store',lazy='dynamic')
    book_id = db.relationship('Book',backref='store',lazy='dynamic')

class Customer(db.Model):
    """This is a customer class or a User class"""
    customer_id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    store_fk_id = db.Column(db.Integer,db.ForeignKey('store.id'))


class Book(db.Model):

    """This is book class. A book can be issued by one to many customers"""
    book_id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    book_name = db.Column(db.String(100),nullable=False)
    store_id = db.Column(db.Integer,db.ForeignKey('store.id'))


class Rental(db.Model):
    """This is a rental class a customer can have one to
    many rentals and one to many books can be rented out manier times"""

    rental_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    rental_charge_per_day = db.Column(db.Integer,nullable=False,default=1)


class RentalItem(db.Model):
    rental_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    issued_on = db.Column(db.DateTime,nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    returned_on = db.Column(db.DateTime,nullable=False)
