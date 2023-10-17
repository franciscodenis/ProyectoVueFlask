from datetime import datetime
from src.core.database import db

class Configuration(db.Model):
    __tablename__ = 'configurations'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    items_per_page = db.Column(db.Integer, nullable=False)
    contact_info = db.Column(db.String(255))
    maintenance_mode = db.Column(db.Boolean, default=False)
    maintenance_message = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )