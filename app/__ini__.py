from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.hello.resource import hello_resource
import config

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

app.register_blueprint(hello_resource)
