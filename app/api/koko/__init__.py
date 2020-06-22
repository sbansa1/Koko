from flask_restx import Namespace

koko_namespace = Namespace('koko')

from app.api.koko import koko_rental_api
