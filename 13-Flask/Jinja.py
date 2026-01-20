### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine

### Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''
from flask import Flask, render_template, request, url_for

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
def resultDis(score):
    res = ""
    if score>=50:
        res = "passed"
    else:
        res = "failed"
    
    return render_template('resultPage.html', result = res) #I need to pass as a new variable, html file wont take an py variable





if __name__ == "__main__":
    app.run(debug=True)
