from flask import Blueprint
from flask import request

api_authentication_bp = Blueprint(
    "authentication_api", __name__, url_prefix="/api/authentication"
)


@api_authentication_bp.route("/", methods=["GET", "POST"])
def authentication():
    incoming_data = request.get_json()
    print("incoming_data: ------>", incoming_data)
    if incoming_data.get("user") and incoming_data.get("password"):
        return {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...."}, 200
    return {"error": "Parámetros inválidos"}, 400
