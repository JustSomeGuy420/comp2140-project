from flask import Blueprint, jsonify, request
from app.models.notification import Notification
from app import db

notification_bp = Blueprint("notification", __name__)

@notification_bp.route("/", methods=["GET"])
def list_notifications():
    notifications = Notification.query.filter_by(is_read=False).all()  # Only unread notifications
    return jsonify([{"id": n.id, "message": n.message, "is_read": n.is_read, "created_at": n.created_at} for n in notifications])

@notification_bp.route("/<int:id>/mark_as_read", methods=["POST"])
def mark_as_read(id):
    notification = Notification.query.get_or_404(id)
    notification.is_read = True
    db.session.commit()
    return jsonify({"message": "Notification marked as read"})