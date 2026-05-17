from flask import Flask
from config import Config
 
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
 
    from tienda.controllers.producto_controller import producto_bp
    app.register_blueprint(producto_bp)
 
    @app.route("/")
    def inicio():
        return "<h1>Tienda en capas</h1><a href='/productos/'>Ver productos</a>"
 
    return app
