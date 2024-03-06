from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/pass/<int:score>')
def pass1(score):
    res=""
    if score>=50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html',result=res)

@app.route('/fail/<int:score>')
def fail1(score):
    return "<html><body><h1>The student Goutham!! has failed with percentage of {0}</h1></body></html>".format(str(score))

@app.route('/results/<int:score>')
def results(score):
    res =""
    if score<=50:
        res = "fail1"
    else:
        res = "pass1"
    return redirect(url_for(res,score=score))

@app.route('/submit',methods=['POST','GET'])
def submit():
    ts = 0
    res = ""
    if request.method=="POST":
        ts = float(request.form['total'])
        if ts<=50:
            res = 'fail1'
        else:
            res = 'pass1'
        return redirect(url_for(res,score=ts))

if __name__=='__main__':
    app.run(debug=True)























# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def welcome():
#     return 'welcome to my first application!!! Gouthamm'

# @app.route('/chocolates')
# def welcome2():
#     return 'welcome to my first application!!! Cholatesa re worthierrrrrrr'


# if __name__=='__main__':
#     app.run(debug=True)

# # print("Hello")