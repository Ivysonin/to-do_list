from flask import Flask

def create_app():
    app = Flask(__name__)


    app.config.from_object('app.config.Config')


    from app.controllers.tarefas_controller import tarefas_bp
    app.register_blueprint(tarefas_bp)

    return app