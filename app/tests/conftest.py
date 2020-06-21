import pytest
from app import create_app
from app.extensions import db

@pytest.fixture(scope="module")
def test_app():
    """Creates the test app"""
    app = create_app(script_info=None)
    app.config.from_object("app.config.TestingConfig")
    with app.app_context():
        yield app

@pytest.fixture(scope="module")
def test_datbase():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()

