from flask import Blueprint, jsonify, request
from app.models.report import Report
from app import db

report_bp = Blueprint("report", __name__)

@report_bp.route("/", methods=["GET"])
def list_reports():
    reports = Report.query.all()
    return jsonify([{"id": r.id, "content": r.content} for r in reports])

@report_bp.route("/", methods=["POST"])
def create_report():
    data = request.json
    new_report = Report(account_id=data["account_id"], content=data["content"])
    db.session.add(new_report)
    db.session.commit()
    return jsonify({"message": "Report created successfully"}), 201