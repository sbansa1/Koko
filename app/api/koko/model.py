from app.extensions import db
import enum

#class Store(db.Model):
   # store_id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
   # customer_id = db.relationship("Customer",backref='store',lazy='dynamic')
   # book_id = db.relationship('Book',backref='store',lazy='dynamic')

class Customer(db.Model):
    """This is a customer class or a User class"""
    customer_id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    #store_fk_id = db.Column(db.Integer,db.ForeignKey('store.id'))
    rental = db.relationship('Rental',backref='cust_book_rented',lazy='dynamic')

class BookType(enum.Enum):
    """Type of Books"""
    REGULAR = 'regular'
    FICTION = 'fiction'
    NOVEL = 'novel'

    @classmethod
    def list(cls):
        return  list(map(lambda c: c.value, cls))

class BookCharge(enum.Enum):
    """Type of Books"""
    REGULAR = 1.5
    FICTION = 3
    NOVEL = 1.5

    @classmethod
    def list(cls):
        return  list(map(lambda c: c.value, cls))

class MinBookCharges(enum.Enum):
    """Min book Charges"""
    REGULAR = 2
    FICTION = 0
    NOVEL = 4.5

    @classmethod
    def list(cls):
        return list(map(lambda x : x.value,cls))


rentalitems = db.Table('rental_items',db.Column('book_id',db.Integer,db.ForeignKey('rental.rental_id')),
                       db.Column('rental_id',db.Integer,db.ForeignKey('book.book_id')))

class Book(db.Model):

    """This is book class. A book can be issued by one to many customers"""
    book_id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    book_name = db.Column(db.String(100),nullable=False)
    book_type=db.Column(db.Enum(BookType,impl=db.String(25)),nullable=False)
    book_charge = db.Column(db.Enum(BookCharge,impl=db.String(10)),nullable=False)
    min_book_charge = db.Column(db.Enum(MinBookCharges,impl=db.String(10)),nullable=False)
    rental = db.relationship('Rental',backref='book_rented',secondary=rentalitems)

    def __init__(self,*args,**kwargs):
        super(Book,self).__init__(*args,**kwargs)


class MinRentDays(enum.Enum):
    REGULAR = 2
    FICTION = 0
    NOVELS = 3

    @classmethod
    def list(cls):
        return list(map(lambda x: x.value, cls))

class Rental(db.Model):
    """This is a rental class a customer can have one to
    many rentals and one to many books can be rented out manier times"""

    rental_id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    rental_charge_per_day = db.Column(db.Integer,nullable=False,default=1)
    min_rent_days = db.Column(db.Enum(MinRentDays,impl=db.String(10)),nullable=False)
    issued_on = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    returned_on = db.Column(db.DateTime, nullable=True)
    books = db.relationship('Book',backref='book_rental',uselist=False,secondary=rentalitems)
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.customer_id'))


    def __init__(self, *args, **kwargs):
        super(Rental, self).__init__(*args, **kwargs)



