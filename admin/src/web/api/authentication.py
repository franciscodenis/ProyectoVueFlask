from flask import Blueprint

api_authentication_bp = Blueprint("authentication_api", __name__, url_prefix="/api/authentication")

@api_authentication_bp.get("/")
def authentication():
    return {"status": "ok"},200