from datetime import datetime
from enum import Enum
from src.core.database import db

class ServiceType(Enum):
    ANALISIS = "ANALISIS"
    CONSULTORIA = "CONSULTORIA"
    DESARROLLO = "DESARROLLO"

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id'), nullable=False)
    institution = db.relationship('Institution', back_populates='services')
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    keywords = db.Column(db.String(255), nullable=False)
    service_type = db.Column(db.Enum(ServiceType), nullable=False)
    enabled = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )