from . import db

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    mac_address = db.Column(db.String(18), unique=True)
    serial_number = db.Column(db.String(100), unique=True)
    manufacturer = db.Column(db.String(100))
    description = db.Column(db.String(1000))

    def __repr__(self):
        return f"<Item {self.name}>"
