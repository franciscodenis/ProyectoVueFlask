from datetime import datetime
from src.core.database import db
from enum import Enum


class ServiceRequestStatus(Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    IN_PROCESS = "IN_PROCESS"
    FINISHED = "FINISHED"
    CANCELED = "CANCELED"


class ServiceRequest(db.Model):
    __tablename__ = "service_requests"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey("services.id"), nullable=False)
    service = db.relationship("Service", back_populates="service_requests", lazy=True)
    user = db.relationship("User", back_populates="service_requests", lazy=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(
        db.Enum(ServiceRequestStatus), default=ServiceRequestStatus.IN_PROCESS
    )
    observation = db.Column(db.String(255))
    notes = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
