from .extentions import db


class ShortUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)
    short_url = db.Column(db.Text, nullable=False, default='Temp')