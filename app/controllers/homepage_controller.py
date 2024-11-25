from flask import Blueprint, flash, render_template, request, url_for

from app.controllers.authentication_controller import login_required
from app import db

# Create a blueprint for account-related routes
homepage_bp = Blueprint("homepage", __name__)

@homepage_bp.route("/")
def index():
    return render_template("index.html")