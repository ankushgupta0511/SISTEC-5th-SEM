from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy         # import database

app = Flask(__name__)


# DATABASE  CONFIGURATION

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# database Model
class user(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    meg = db.Column(db.String(120), nullable=True)

with app.app_context():
    db.create_all()

@app.route('/register',methods=['GET','POST'])
def register():

    return render_template('register.html')



if __name__=='__main__':
    app.run(debug=True)

