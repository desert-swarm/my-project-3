from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app) 

from db_app2.catalog.views import catalog 
app.register_blueprint(catalog)
with app.app_context():
    db.create_all() 

    