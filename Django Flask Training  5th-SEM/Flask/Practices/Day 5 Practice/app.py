from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy         # import database

app = Flask(__name__)


# DATABASE  CONFIGURATION

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/register'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(12), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            print(name,email,password)

            # adding data in databse
            print('0')
            entry = User(name=name,email=email,password=password)
            print('1')
            db.session.add(entry)
            print('2')
            db.session.commit()
            print('Data Successfully added!!')

        except Exception as e:
            print('Errors occure!!')

    return render_template('register.html')



if __name__=='__main__':
    app.run(debug=True)

