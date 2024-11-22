from app import db

class Notification(db.Model):
    """
    Notification model for system or user notifications.
    """
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    message = db.Column(db.String(255), nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    account = db.relationship("Account", backref=db.backref("notifications", lazy=True))

    def __repr__(self):
        return f"<Notification {self.id}>"