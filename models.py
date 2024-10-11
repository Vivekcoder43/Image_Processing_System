
from app import db

class Request(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    status = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.String(36), db.ForeignKey('request.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    input_urls = db.Column(db.Text, nullable=False)
    output_urls = db.Column(db.Text)
