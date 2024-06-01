from flask import Flask, render_template, request, session


def create_app():
    app = Flask(__name__, static_folder="static")
    app.config["SECRET_KEY"] = "test123"

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
