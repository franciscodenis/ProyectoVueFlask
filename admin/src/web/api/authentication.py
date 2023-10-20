from flask import Blueprint
from flask import request
from src.web.schemas.authentication import user_schema

api_authentication_bp = Blueprint("authentication_api", __name__, url_prefix="/api/authentication")

@api_authentication_bp.route("/",methods=['GET', 'POST'])
def authentication():
    incoming_data = request.get_json()
    user_authentication = user_schema.load(incoming_data)
    return {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...."
        },200

