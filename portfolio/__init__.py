from flask import Flask


def create_app():
    app = Flask(__name__)

    from .views import views
    from .projects import projects
    from .tutorials import tutorials

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(projects, url_prefix='/project')
    app.register_blueprint(tutorials, url_prefix='/tutorial')

    return app
