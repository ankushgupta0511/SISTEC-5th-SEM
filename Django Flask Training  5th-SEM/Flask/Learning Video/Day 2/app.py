from flask import Flask,redirect,url_for

app = Flask(__name__)  # create app

# # dynemic url
# @app.route('/success/<int:score>')
# def success(score):
#     return f"<h1>My 12th score is : {score} And Student Is  </h1> <h2>{'Fail' if score < 50 else 'Pass' }</h2> " 



# dynemic url
@app.route('/success/<int:score>')
def success(score):
    return "<h1>My 12th score is : </h2> " +str(score) +"<h1> Pass </h1> "  


# dynemic url
@app.route('/fail/<int:score>')
def fail(score):
    return "<h1>My 12th score is : </h2> " + str(score) +"<h1> Fail </h1> "  



# dynemic url
@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks > 50:
        result = 'success'
    else:
        result = 'fail'

    return redirect(url_for(result,score=marks))



if __name__=='__main__':
    # print(__name__)
    app.run(debug=True)

