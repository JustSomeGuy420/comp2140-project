from flask import Blueprint, jsonify, request
from app.models.appointment import Appointment
from app import db

appointment_bp = Blueprint("appointment", __name__)

@appointment_bp.route("/", methods=["GET"])
def list_appointments():
    appointments = Appointment.query.all()
    return jsonify([{"id": a.id, "date": a.date, "description": a.description} for a in appointments])

@appointment_bp.route("/", methods=["POST"])
def create_appointment():
    data = request.json
    new_appointment = Appointment(
        account_id=data["account_id"],
        date=data["date"],
        description=data.get("description"),
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({"message": "Appointment created successfully"}), 201