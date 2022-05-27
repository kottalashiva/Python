from flashMarket import db, login_manager
from flashMarket import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), unique=True, nullable=False)
    barcode = db.Column(db.String(length=12), unique=True, nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=250), unique=False, nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'

    def buy(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()

    def sell(self, user):
        self.owner = None
        user.budget += self.price
        db.session.commit()

class User(db.Model, UserMixin):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), unique=True, nullable=False)
    email_field = db.Column(db.String(length=50), unique=True, nullable=False)
    password = db.Column(db.String(length=16), unique=False, nullable=False)
    budget = db.Column(db.Integer(), default=15000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'{self.name}'

    @property
    def pswd(self):
        return self.password

    @pswd.setter
    def pswd(self, attempted_password):
        self.password = bcrypt.generate_password_hash(attempted_password).decode('UTF-8')

    def compare_password(self, form_password):
        return bcrypt.check_password_hash(self.password,form_password)

    def can_purchase(self, item):
        return self.budget > item.price

    def can_sell(self, item):
        return item in self.items
