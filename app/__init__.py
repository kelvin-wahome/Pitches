from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

def create_app(config_name):
    app = Flask(__name__)


# initializing flask extensions
bootstrap.iniy_app(app)
db.init_app(app)

bootstrap = Bootstrap()
db = SQLAlchemy()
