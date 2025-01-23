
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Livre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(150), nullable=False)
    auteur = db.Column(db.String(150), nullable=False)
    annee_publication = db.Column(db.Integer, nullable=False
