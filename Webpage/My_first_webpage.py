from flask import Flask, render_template  #importing the flask and render_template functions    #install flask by pip install flask

app = Flask(__name__)  #creating the flask app

@app.route("/") #mentioning the link name
def home():  #Function for calling wih name
    return render_template("home.html") #it takes the script from home.html

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":  #checking the condition
    app.run(debug = True)  #calling the app and running it
    
