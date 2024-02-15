from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True # 开启debug模式

import pymysql
pymysql.install_as_MySQLdb() 

from config import DBConfig
from flask_sqlalchemy import SQLAlchemy
app.config.from_object(DBConfig)
db = SQLAlchemy(app)