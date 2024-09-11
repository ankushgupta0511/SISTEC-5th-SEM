from flask import Flask, redirect, url_for,render_template,request
app = Flask(__name__)




# dynemic url
@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks > 50:
        result = 'pass'
    else:
        result = 'fail'

    return render_template('result.html',res=result)





if __name__=='__main__':
    app.run(debug=True)