from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.db_setup import db
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            flash("Giriş başarılı!", "success")
            return redirect(url_for('index'))
        else:
            flash("Hatalı e-posta veya şifre!", "danger")
    
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash("Kayıt başarılı! Giriş yapabilirsiniz.", "success")
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')
