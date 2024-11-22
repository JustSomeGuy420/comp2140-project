from flask import Blueprint, render_template, request, jsonify

# Create a blueprint for account-related routes
account_bp = Blueprint("account", __name__)

@account_bp.route("/")
def list_accounts():
    """
    Example route: List all accounts.
    """
    # Fetch accounts from the database (replace with real logic)
    accounts = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]
    return jsonify(accounts)

@account_bp.route("/<int:id>")
def account_details(id):
    """
    Example route: Get details for a single account.
    """
    # Fetch account by ID (replace with real logic)
    account = {"id": id, "name": "John Doe", "email": "john@example.com"}
    return jsonify(account)