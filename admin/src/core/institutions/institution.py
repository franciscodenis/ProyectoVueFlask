from datetime import datetime
from src.core.database import db

class Institution(db.Model):
    __tablename__ = "institutions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))
    information = db.Column(db.String(255))
    address = db.Column(db.String(255))
    location = db.Column(db.String(255))
    web = db.Column(db.String(100))
    keywords = db.Column(db.String(100))
    opening_hours = db.Column(db.String(100))
    contact = db.Column(db.String(100))
    has_authorization = db.Column(db.Boolean)
    services = db.relationship('Service', back_populates='institution')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )