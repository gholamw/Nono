from flask_login import LoginManager
from flask_wtf import Form
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_script import Manager
#from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__, static_url_path='/static')
Bootstrap(app)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'you-will-never-guess'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
#app.run(threaded=True)
db = SQLAlchemy(app)
#migrate = Migrate(app, db)
manager = Manager(app)
#manager.add_command('db', MigrateCommand)
db.create_all()

lm = LoginManager(app) #login manager
lm.init_app(app)


from app import views, models

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    #file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    #file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    #app.logger.setLevel(logging.INFO)
    #file_handler.setLevel(logging.INFO)
    #app.logger.addHandler(file_handler)
    #app.logger.info('microblog startup')
