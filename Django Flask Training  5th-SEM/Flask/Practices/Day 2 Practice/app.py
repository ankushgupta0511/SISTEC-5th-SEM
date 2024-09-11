from flask import Flask,redirect,url_for

app = Flask(__name__)  # create app



@app.route('/less100/<int:num>')
def less100(num):
    return f"Number {num} Less than 100. "



@app.route('/less200/<int:num>')
def less200(num):
    return f"Number {num} Less than 200. "



@app.route('/less300/<int:num>')
def less300(num):
    return f"Number {num} Less than 300. "



@app.route('/more299/<int:num>')
def more299(num):
    return f"Number {num} more than  299."


@app.route('/main/<int:marks>')
def main(marks):
    print('ankush')
    main = ""
    if marks < 100:
        main = 'less100'
    elif marks > 99 and marks < 200:
        main = 'less200'
    else:
        main = 'more299'

    return redirect(url_for(main,num=marks))





if __name__=='__main__':
    # print(__name__)
    app.run(debug=True)

