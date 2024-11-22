from flask import Blueprint, jsonify, request
from app.models.notice import Notice
from app import db

notice_bp = Blueprint("notice", __name__)

@notice_bp.route("/", methods=["GET"])
def list_notices():
    notices = Notice.query.all()
    return jsonify([{"id": n.id, "title": n.title, "content": n.content} for n in notices])

@notice_bp.route("/", methods=["POST"])
def create_notice():
    data = request.json
    new_notice = Notice(title=data["title"], content=data["content"])
    db.session.add(new_notice)
    db.session.commit()
    return jsonify({"message": "Notice created successfully"}), 201