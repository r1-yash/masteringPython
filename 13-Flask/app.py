from flask import Flask
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''

app = Flask(__name__) #1. web app as object

@app.route("/")
def welcome():
    return "THis will be the first page"

@app.route("/home")
def home():
    return "This takes our page to /home since app route is given that "

if __name__ == "__main__": #1 basic template for every flask 
    app.run(debug=True) #this debug true practice is only for page refresh during 
