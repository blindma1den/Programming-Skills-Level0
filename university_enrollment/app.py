from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms import StringField, PasswordField, SubmitField, SelectField


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.secret_key = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    program = db.Column(db.Integer, db.ForeignKey('program.id'))
    login_attempts = db.Column(db.Integer, default=0)
    is_locked = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Campus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100))

    def __repr__(self):
        return f'<Campus {self.city}>'

class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    campus = db.Column(db.Integer, db.ForeignKey('campus.id'))
    available_seats = db.Column(db.Integer, default=5)

    def __repr__(self):
        return f'<Program {self.name}>'
    
class registration_form(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    campus = SelectField('Campus', coerce=int)
    program = SelectField('Program', coerce=int)
    submit = SubmitField('Register')

class login_form(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-programs/<int:campus_id>')
def get_programs(campus_id):
    programs = Program.query.filter_by(campus=campus_id).all()
    program_list = [(program.id, program.name) for program in programs]
    return jsonify(program_list)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registration_form()
    form.campus.choices = [(campus.id, campus.city) for campus in Campus.query.all()]
    form.program.choices = [(program.id, program.name) for program in Program.query.all()]
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data, program=form.program.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = login_form()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('home'))
            else:
                user.login_attempts += 1
                db.session.commit()
                if user.login_attempts >= 3:
                    user.is_locked = True
                    db.session.commit()
                    flash('User is locked') 
                db.session.commit()
                flash('Invalid password')
        else:
            flash('User not found')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)