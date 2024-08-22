from routes.home import home_route
from routes.cliente import cliente_route
from database.database import db
from database.models.cliente import Cliente

def general_config(app):
    routes_config(app)
    db_config()


def routes_config(app):
    #rotas
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix = '/clientes')


def db_config():
    db.connect()
    db.create_tables([Cliente])


