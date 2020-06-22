from app.api.koko.model import Rental,Book,Customer
from app.extensions import db

def all_rental_by_customer(customer_id):
    """Gets all the books rented by the customer"""
    all_books_query = Rental.query.join(Book,Rental.books)
    all_books_query = all_books_query.filter(Rental.customer_id==customer_id).order_by(Rental.issued_on).all()
    return all_books_query
