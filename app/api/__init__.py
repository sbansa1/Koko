from flask_restx import Api

api = Api(version=1.0,description="An API for KOKO",title="Koko API", doc="/")


from app.api.ping import ping_namespace

api.add_namespace(ping_namespace)