import datetime
from turtle import title
from wsgiref.validate import validator
from flask import Flask, render_template, flash, url_for, redirect
# from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
from sqlalchemy.exc import SQLAlchemyError
#from app import db

# The following command imports a CLASS: SignUpForm from form.py file:
# from form import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "YOU-WILL-NEVER-KNOW"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
#####
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
#####
login_manager.init_app
######
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# with app.app_context():
#     db.create_all()

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), nullable= False, unique=True)
    #, unique=True
    email = db.Column(db.String(50), nullable= False, unique=True)
    #, unique=True
    password_hash = db.Column(db.String(80), nullable= False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    joined_date = db.Column(db.DateTime, default= datetime.datetime.utcnow)
    location = db.Column(db.String(50), nullable= False)
    bio= db.Column(db.String(500), nullable=True)
    groups= db.relationship('Group', backref='creator', lazy='dynamic')
    events= db.relationship('Event',backref= 'host', lazy= 'dynamic')



    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        print(self.password_hash)
        print(password)
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return '<Post {}>'.format(self.message)

class Group(db.Model):
    __tablename__ = "group"
    id= db.Column(db.Integer, primary_key=True)
    groupName= db.Column(db.String(150), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    events= db.relationship('Event',backref= 'group', lazy= 'dynamic')
    #event_id


    def __repr__(self) -> str:
        return '<Group {}>'.format(self.groupName)

class Event(db.Model):
    __tablename__ = "event"
    id= db.Column(db.Integer, primary_key=True)
    eventName= db.Column(db.String(150), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow())
    time= db.Column(db.String(50), nullable= False)
    location= db.Column(db.String(50), nullable= False)
    description= db.Column(db.String(500), nullable=True)

    host_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    group_id= db.Column(db.Integer, db.ForeignKey('group.id'))
    #attendees
    #event_id



    def __repr__(self) -> str:
        return '<Event {}>'.format(self.eventName)

class SignUpForm(FlaskForm):
    username = StringField('Name', render_kw={'placeholder': 'Please input Name'}, validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', validators=[DataRequired(), EqualTo('confirm', message= 'Passwords must match')])
    confirm = PasswordField('Confirm Password')
    location= StringField('Location', render_kw={'placeholder': 'Please input city'}, validators= [DataRequired()])
    bio= StringField('Bio', render_kw={'placeholder': 'Optional Bio'})
    submit = SubmitField('Sign Up')
    
class LoginForm(FlaskForm):
    # username = StringField('Username', render_kw={'placeholder': 'Please input Name'}, validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Post')

class GroupForm(FlaskForm):
    groupName= StringField('Group Name', validators=[DataRequired()])
    submit= SubmitField('Create Group')

class EventForm(FlaskForm):
    eventName = StringField('Event Name', render_kw={'placeholder': 'Please input name'}, validators=[DataRequired()])
    time = StringField('Time', render_kw={'placeholder': 'Please input location'}, validators=[DataRequired()])
    location= StringField('Location', render_kw={'placeholder': 'Please input location'}, validators= [DataRequired()])
    description= StringField('Description', render_kw={'placeholder': 'Please input event description'})
    submit = SubmitField('Create Event')

@app.route("/")
def home():
    return render_template("first.html")
    #return "Hello"

@app.route("/first/")
def first():
    return "Hello"
    #return render_template("first.html")

@app.route("/list/")
def list():
    return render_template("list.html")

@app.route("/signup/", methods=['GET', 'POST'] )
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(username=form.username.data, email=form.email.data, location= form.location.data, bio= form.bio.data)
            user.set_password(form.password.data)
            ####added try and exception statements
            try: 
                db.session.add(user)
                db.session.commit()
            except SQLAlchemyError as e:
                reason= str(e)
                return reason
            login_user(user)
            return '<h1>New User has been created!</h1> <br> <a href= /> Back</a>'  
        flash("A user already exists with that email address.")
        print("A user already exists with that email address.")
    return render_template("signup.html", title="Sign Up Page", form = form)

@app.route("/login/", methods=['GET', 'POST'] )
def login():
    form = LoginForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        
        if existing_user is None or not existing_user.check_password(form.password.data):
            flash("Invalid username or password!")
            print("Invalid username or password!")
            #return redirect(url_for('events'))
            return render_template("login.html", form=form)

        login_user(existing_user, remember=form.remember_me.data)
        #user = User(username=form.username.data, email=form.email.data)
        flash("Successful!")
        print("Successful!")
        ##### changed first to events page
        return redirect(url_for('user_home', username=current_user.username))

    flash("Failure")
    print("Failure")
    return render_template("login.html", title="Login Page", form = form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/event/<eventName>", methods=['GET', 'POST'] )
def event(eventName):
    return render_template("event.html", event= eventName)

@app.route("/user/")
@app.route("/user/<username>", methods=['GET', 'POST'] )
@login_required
def user_home(username):
    form = PostForm()
    if form.validate_on_submit():
        #message = form.message.data 
        #user = User.query.filter_by(username=username).first()
        #print(message)
        #print(user)
        # _or_404
        # user_id = user.id
        ####post= Post(message)
        post = Post(message=form.message.data, user_id= User.query.filter_by(username=username).first())
        print(post)

        db.session.add(post)
        db.session.commit()
    groups= current_user.groups
    allGroups= Group.query.all()
    #posts = Post.query.all()
    
    #return render_template("first.html")
    return render_template("user_home.html", form=form, username=current_user.username, groups= groups, allGroups= allGroups) #, posts=posts

@app.route("/user/")
@app.route("/user/<username>/profile", methods=['GET', 'POST'] )
@login_required
def profile(username):
    return render_template("profile.html", username=username)

@app.route("/user/")
@app.route("/user/<username>/groups", methods=['GET', 'POST'] )
@login_required
def groups(username):
    return render_template("groups.html", username=username)

@app.route("/user/")
@app.route("/user/<username>/viewGroup/<groupName>", methods=['GET', 'POST'] )
@login_required
def viewGroup(groupName, username):
    group_id= Group.query.filter_by(groupName=groupName).first().id
    events= Group.query.get(group_id).events
    return render_template("viewGroup.html", group=groupName, username=username, events= events)

@app.route("/user/")
@app.route("/user/<username>/createGroup/<groupName>/createEvent", methods=['GET', 'POST'] )
@login_required
def createEvent(username, groupName):
    form = EventForm()
    if form.validate_on_submit():
        existing_event = Event.query.filter_by(eventName=form.eventName.data).first()
        if existing_event is None:
            host= User.query.filter_by(username=username).first()
            group= Group.query.filter_by(groupName= groupName).first()
            event= Event(eventName= form.eventName.data, time= form.time.data, location= form.location.data, description= form.description.data, host_id= host.id, group_id=group.id)
            db.session.add(event)
            db.session.commit()
            return '<h1>New Event has been created!</h1> <br> <a href=/user/<username>/viewGroup/<groupName> Back</a>' 
        print("Event already exists with that name")
    print(form.errors)
    return render_template("createEvent.html", username=username, form= form, groupName= groupName)


@app.route("/user/")
@app.route("/user/<username>/createGroup", methods=['GET', 'POST'] )
@login_required
def createGroup(username):
    form = GroupForm()
    if form.validate_on_submit():
        existing_group = Group.query.filter_by(groupName=form.groupName.data).first()
        if existing_group is None:
            user= User.query.filter_by(username=username).first()
            group= Group(groupName= form.groupName.data, user_id= user.id)
            db.session.add(group)
            db.session.commit()
            groups=Group.query.all()
            #return render_template("groups.html", form = form, username=username, groups=groups)
            return '<h1>New Group has been created!</h1> <br> <a href= /user/<username> Back</a>' 
        print("Group already exists with that name")
    return render_template("createGroup.html", username=username, form= form)


if __name__ == "__main__":
    app.run(debug=True)