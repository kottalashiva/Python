from flask import render_template, redirect,url_for, flash, request
from flashMarket import app
from flashMarket import db
from flashMarket.forms import RegisterForm,LoginForm, PurchseForm, SellForm
from flashMarket.models import Item, User
from flask_login import login_user, logout_user, login_required,current_user



@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/market',methods=['GET', 'POST'])
@login_required
def market():
    purchase_form = PurchseForm()
    sell_form = SellForm()
    if request.method == 'POST':
        purchased_item = request.form.get('purchased_item')
        p_item_data = Item.query.filter_by(name=purchased_item).first()
        if p_item_data:
            if current_user.can_purchase(p_item_data):
                p_item_data.buy(current_user)
                flash('Successfully purcased the product')
        sold_item = request.form.get('sold_item')
        s_item_data = Item.query.filter_by(name=sold_item).first()
        if s_item_data:
            if current_user.can_sell(s_item_data):
                s_item_data.sell(current_user)
                flash('Successfully Sold the product')
        return redirect(url_for('market'))
    if request.method == 'GET':
        item_data = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', item_data=item_data, purchase_form=purchase_form, sell_form=sell_form, owned_items=owned_items)

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email_field=form.email.data, pswd=form.password1.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('market'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f' {err_msg}', category='danger')
            print(f'There are few errors in the form {err_msg}')
    return render_template('register_user.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user and user.compare_password(form.password.data):
            login_user(user)
            flash('Success logged In', category='success')
            return redirect(url_for('market'))
        else:
            flash('Invalid Credentails', category='danger')
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There are few errors in the form {err_msg}', category='danger')
            print(f'There are few errors in the form {err_msg}')

    return render_template('login_user.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('Logged out successfully', category='success')
    return redirect(url_for('home'))
