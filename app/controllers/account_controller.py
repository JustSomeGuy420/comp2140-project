from flask import Blueprint, jsonify, request, flash, render_template
from app.models.account import Account
from app import db

# Create a blueprint for account-related routes
account_bp = Blueprint("account", __name__)

@account_bp.route("/")
def list_accounts():
    accounts = Account.query.all()
    return jsonify([{"name": a.name, "username": a.username, "hall": a.hall} for a in accounts])

@account_bp.route("/<int:id>/subscribe", methods=["POST"])
def subscribe(id):
    account = Account.query.get_or_404(id)

    # Only allow subscription if the user is logged in and is the account owner
    if account.id != session.get('user_id'):
        flash("You are not authorized to manage this subscription.")
        return redirect(url_for("account.account_details", id=account.id))

    # Set subscription to True to opt-in for notifications
    if not account.subscription:
        account.subscription = True
        db.session.commit()
        flash(f"Subscription successful for {account.name}. You will receive notifications.")
    else:
        flash("You are already subscribed.")

    return redirect(url_for("appointment.create_appointment"))
    
@account_bp.route("/<int:id>")
def account_details(id):
    account = Account.query.get(id)
    return jsonify({"name": account.name, "email": account.email})

@account_bp.route('/loyalty')
def loyalty():
    return render_template('account/loyal.html')

def add_points(account:Account):
    account.points += 5
    check_status(account)

def check_status(account:Account):
    # Update status based on points
    if account.points >= 400:
        account.status = 'Free Wash And Dry!'
    elif account.points >= 200:
        account.status = 'Free Wash Or Dry!'
    elif account.points >= 100:
        account.status = '50 Percent Off Next Wash Or Dry!'
    elif account.points >= 50:
        account.status = '20 Percent Off Next Wash Or Dry!'
    else:
        account.status = 'No Discount Yet'
    
    db.session.commit()

def redeem_points(account:Account, reward):
    # Redeem points for rewards
    if account.points >= reward['points']:
        account.points -= reward['points']
        account.rewards.append(reward)
        account.check_status()  # Update status after redeeming
        flash(f"{account.name} redeemed {reward['name']} for {reward['points']} points.")
        return True
    flash(f"{account.name} does not have enough points to redeem {reward['name']}.")
    return False