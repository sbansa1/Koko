from flask.cli import FlaskGroup
from app import create_app
from app.api.koko.model import Book, Rental, BookCharge, MinRentDays, MinBookCharges, BookType, Customer
from app.extensions import db
import datetime

app = create_app()
cli = FlaskGroup(create_app=create_app)

x = datetime.datetime.now() - datetime.timedelta(days=7)
y = datetime.datetime.now() - datetime.timedelta(days=2)
z = datetime.datetime.now() - datetime.timedelta(days=4)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
@cli.command("seed_db")
def seed_db():
    """Seeds the database"""
    db.session.add(Customer())
    book1 = Book(book_name="Shake-Bake",book_type=BookType.REGULAR,book_charge=BookCharge.REGULAR,min_book_charge=MinBookCharges.REGULAR)
    book2 = Book(book_name="Tom-Jerry",book_type=BookType.FICTION,book_charge=BookCharge.FICTION,min_book_charge=MinBookCharges.FICTION)
    book3 = Book(book_name="Titanic",book_type=BookType.NOVEL,book_charge=BookCharge.NOVEL,min_book_charge=MinBookCharges.NOVEL)

    rental1 = Rental(min_rent_days=MinRentDays.REGULAR,quantity=7,issued_on=x,returned_on=datetime.datetime.today(),customer_id=1)
    book1.rental.append(rental1)
    db.session.add(book1)
    rental2 = Rental(min_rent_days=MinRentDays.FICTION,issued_on=y,quantity=2,returned_on=datetime.datetime.today(),customer_id=1)
    book2.rental.append(rental2)
    db.session.add(book2)
    rental3 = Rental(min_rent_days=MinRentDays.NOVELS,issued_on=z,quantity=4,returned_on=datetime.datetime.today(),customer_id=1)
    book3.rental.append(rental3)
    db.session.add(book3)
    db.session.commit()


if __name__=="__main__":
    cli()