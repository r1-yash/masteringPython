from flask import Flask, render_template, request
#request is how Flask looks at what came from the HTML page (the browser).

app = Flask(__name__)

@app.route("/")
def welcome():
    return "First welcome page"

@app.route("/base", methods =['GET'])
def base():
    return render_template('base.html')


#here the request.form gets me the value of variable and /form takes that from where to take this 

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

# @app.route("/submit"mf, methods=['GET', 'POST'])
# def submit():
#     if request.method=='POST':
#         name = request.form['name']
#         return f'Hello {name}'
#     return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)