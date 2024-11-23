from flask import Blueprint, jsonify, request
from app.models.account import Account
from app import db

# Create a blueprint for account-related routes
account_bp = Blueprint("account", __name__)

@account_bp.route("/")
def list_accounts():
    accounts = Account.query.all()
    return jsonify([{"id": a.id, "date": a.name, "description": a.email} for a in accounts])

@account_bp.route("/<int:id>")
def account_details(id):
    account = Account.query.get_or_404(id)
    return jsonify({"id": account.id, "date": account.name, "description": account.email})