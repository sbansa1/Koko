from flask_restx import Namespace

ping_namespace = Namespace("ping",description="Testing..")

from app.api.ping import views