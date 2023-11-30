from .database import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String, unique=False, nullable=True)

    def __repr__(self):
        return '<Product %r>' % self.name
