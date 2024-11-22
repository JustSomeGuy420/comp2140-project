from app import db

class Appointment(db.Model):
    """
    Appointment model to store scheduling details.
    """
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    account = db.relationship("Account", backref=db.backref("appointments", lazy=True))

    def __repr__(self):
        return f"<Appointment {self.id} for Account {self.account_id}>"