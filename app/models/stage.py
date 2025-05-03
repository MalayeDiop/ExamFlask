from app import db
from datetime import date

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entreprise = db.Column(db.String(150), nullable=False)
    poste = db.Column(db.String(100), nullable=False)
    debut = db.Column(db.Date, nullable=False)  # <- bien en db.Date
    fin = db.Column(db.Date)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
