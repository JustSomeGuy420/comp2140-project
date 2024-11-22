from flask import Blueprint, jsonify, request
from app.models.timer import Timer
from app import db

timer_bp = Blueprint("timer", __name__)

@timer_bp.route("/", methods=["GET"])
def list_timers():
    timers = Timer.query.all()
    return jsonify([{"id": t.id, "name": t.name, "duration": t.duration} for t in timers])

@timer_bp.route("/", methods=["POST"])
def create_timer():
    data = request.json
    new_timer = Timer(name=data["name"], duration=data["duration"])
    db.session.add(new_timer)
    db.session.commit()
    return jsonify({"message": "Timer created successfully"}), 201