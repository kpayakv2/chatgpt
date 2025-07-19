from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# SQLAlchemy database instance
# Initialized in app.py via db.init_app(app)
db = SQLAlchemy()

class MaintenanceLog(db.Model):
    """Model for recording maintenance logs."""
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow)
    part = db.Column(db.String(100), nullable=False)
    mileage = db.Column(db.Integer)
    notes = db.Column(db.String(200))

