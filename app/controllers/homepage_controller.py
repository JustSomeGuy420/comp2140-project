from flask import Blueprint, render_template, request, jsonify

# Create a blueprint for account-related routes
homepage_bp = Blueprint("Homepage", __name__)

@homepage_bp.route("/")
def show_homepage():
    return "Hello World"