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
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    keywords = db.Column(db.String(255), nullable=False)
    service_type = db.Column(db.Enum(ServiceType), nullable=False)
    enabled = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    """
    # Relación muchos a muchos con los centros habilitados
    instituciones = db.relationship('Institucion', secondary='service_center', back_populates='services')

    Definición de la tabla intermedia 'service_center'
    service_center = db.Table(
    'service_center',
    db.Column('service_id', db.Integer, db.ForeignKey('service.id')),
    db.Column('insitucion', db.Integer, db.ForeignKey('institucion.id'))
)"""