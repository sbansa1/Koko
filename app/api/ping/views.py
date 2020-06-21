from app.api.ping import ping_namespace
from flask_restx import Resource


class PingResource(Resource):

    @ping_namespace.response(code=200,description="ping")
    def get(self):
        """Just checking if the project is set up correctly"""
        return {'msg':"Ping!"},200


ping_namespace.add_resource(PingResource,"/")