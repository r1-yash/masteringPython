### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine

### Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def welcome():
    return "this will be my first page"

@app.route("/resultPage/<int:score>")
def resultDis(score):
    res = ""
    if score>=50:
        res = "passed"
    else:
        res = "failed"
    
    return render_template('resultPage.html', result = res) #I need to pass as a new variable, html file wont take an py variable

@app.route("/successres/<int:score>")
def succres(score):
    res = ""
    if score>=50:
        res = "passed"
    else:
        res = "failed"

    dict = {'score':score, 'result':res}
    
    return render_template('resultPage1.html', result = dict) #I need to pass as a new variable, html file wont take an py variable

@app.route("/resultif/<int:score>")
def resif(score):

    
    return render_template('resultPage2.html', result = score) #I need to pass as a new variable, html file wont take an py variable

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('succres',score=total_score))

#successres gave ERRROR why ?? because   
#In url_for, you give the function name (endpoint name), not the URL path.



if __name__ == "__main__":
    app.run(debug=True)
