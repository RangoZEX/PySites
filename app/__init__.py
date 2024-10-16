from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes from the routes module
    from .routes import home_route
    app.register_blueprint(home_route)

    return app
