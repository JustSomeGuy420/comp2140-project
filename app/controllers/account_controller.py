from flask import Blueprint, jsonify, request
from app.models.account import Account
from app import db

# Create a blueprint for account-related routes
account_bp = Blueprint("account", __name__)

@account_bp.route("/")
def list_accounts():
    accounts = Account.query.all()
    return jsonify([{"name": a.name, "username": a.username, "hall": a.hall} for a in accounts])

@account_bp.route("/<int:id>")
def account_details(id):
    account = Account.query.get(id)
    return jsonify({"name": account.name, "email": account.email})