from .db import db

class Customer(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.String, primary_key=True)
    company_name = db.Column(db.String)
    contact_name = db.Column(db.String)
    contact_title = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    country = db.Column(db.String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
