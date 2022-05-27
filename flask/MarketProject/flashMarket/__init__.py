from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required

app = Flask(__name__)
# sqlite:///MarketItem.db
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY']  = '09afe9db0bba9ef2143c475f'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user_login'
login_manager.login_message_category   = 'warning'

from flashMarket import routes
