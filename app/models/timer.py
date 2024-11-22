from app import db

class Timer(db.Model):
    """
    Timer model for managing timed events.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in seconds
    created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f"<Timer {self.name} ({self.duration}s)>"