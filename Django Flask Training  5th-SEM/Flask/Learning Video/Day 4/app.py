from flask import Flask,redirect,url_for,render_template,request
app  = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')



# dynemic url
@app.route('/result/<int:marks>')
def result(marks):
    print(marks)
    result = ""
    if marks > 50:
        result = 'Pass'
    else:
        result = 'Fail'

    return render_template('result.html',res=result)




@app.route('/submit',methods=['GET','POST'])
def submit():
    totoal_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        math = float(request.form['math'])
        python = float(request.form['python'])
        django = float(request.form['django'])
        totoal_score = (science+math+python+django)/4
        print(science,math,python,django,totoal_score)
        return redirect(url_for('result',marks=totoal_score))



if __name__=='__main__':
    app.run(debug=True)
