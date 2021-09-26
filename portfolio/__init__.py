from flask import Flask


def create_app():
    app = Flask(__name__)

    from .views import views
    from .projects import projects

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(projects, url_prefix='/projects')

    return app
