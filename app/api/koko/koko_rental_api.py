from flask_restx import Resource
from app.api.koko import koko_namespace
from app.api.koko.crud import  all_rental_by_customer
from app.api.koko.koko_utils import calculate_total_rent


class ApiResource(Resource):
    """A namespace for the API"""

    def get(self):
        data = all_rental_by_customer(customer_id=1)
        total = (calculate_total_rent(data))

        return {"total_amount":total},200

koko_namespace.add_resource(ApiResource,"/total")