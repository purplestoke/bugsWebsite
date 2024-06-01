from flask import Flask, render_template, request, Blueprint, jsonify


views = Blueprint("views", __name__)


# HOMEPAGE
@views.route("/")
def home():
    return render_template("home.html")


# ABOUT PAGE
@views.route("/about")
def about():
    return render_template("about.html")


# EVENTS PAGE
@views.route("/events")
def events():
    return render_template("events.html")


# STOKE PAGE
@views.route("/stoke")
def stoke():
    return render_template("stoke.html")


# WALLETS PAGE
@views.route("/wallets")
def wallets():
    return render_template("wallets.html")


# SERVERS PAGE
@views.route("/servers")
def servers():
    return render_template("servers.html")


# CONTACT PAGE
@views.route("/contact")
def contact():
    return render_template("contact.html")


# CREATOR PAGE
@views.route("/creator")
def creator():
    return render_template("creator.html")


# FUND US PAGE
@views.route("/fund")
def fund():
    return render_template("fund.html")
