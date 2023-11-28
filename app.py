from flask import Flask, render_template
# from flask_cors import CORS
from extensions import db
from entrega.entrega_controller import EntregaController
from config.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    entrega_controller = EntregaController()
    app.register_blueprint(entrega_controller.bp)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    # CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Swagger(app)

    return app

aplication = create_app()

if __name__ == "__main__":
    aplication.run(debug=True)
