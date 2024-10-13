from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
#initializing flask
app = Flask(__name__)
#for security having session key
app.config['SECRET_KEY'] = 'd28a75bbf5fc10e49f35c7587ed79bcb50d977f0c2efd98a'
app.config['JWT_SECRET_KEY'] = '9875521d3512d262fef614dbe6951086b47edaae0c14cf16'
#connecting db2
app.config['SQLALCHEMY_DATABASE_URI'] = 'ibm_db_sa://db2admin:pain@localhost:50000/Fingen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

#to add user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
#flask to create db
with app.app_context():
    db.create_all()

