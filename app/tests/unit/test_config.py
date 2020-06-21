import os


def test_testing_config(test_app):
    """this tests the configuration variables"""
    assert test_app.config['SECRET_KEY'] == "my_precious"
    assert test_app.config['TESTING'] == True
    assert test_app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_TEST_URL')
    assert not test_app.config.get('Development')


def test_development_config(test_app):
    """This tests the development config"""

    assert test_app.config.get("SECRET_KEY") == "my_precious"
    assert test_app.config.get('SQLALCHEMY_DATABASE_URI') == os.environ.get('DATABASE_URL')
    assert not test_app.config.get('Production')
    assert not test_app.config.get('Testing')


def test_production_config(test_app):
    """Tests the production config"""
    assert test_app.config.get('SECRET_KEY') == "my_precious"
    assert test_app.config.get('SQLALCHEMY_DATABASE_URI') == os.environ.get('DATABASE_URL')
    assert not test_app.config.get('Development')
    assert not test_app.config.get('Testing')