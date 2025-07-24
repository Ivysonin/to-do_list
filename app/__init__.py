from flask import Flask

def create_app():
    app = Flask(__name__)


    app.config.from_object('app.config.Config')


    from app.controllers.tarefas_controller import tarefas_bp
    app.register_blueprint(tarefas_bp)
    from app.controllers.home_controller import home_bp
    app.register_blueprint(home_bp)

    return app