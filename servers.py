from calendar import c
from turtle import color
from flask import Flask, render_template   # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<your_name>')
def say(your_name):
    return 'Hi '+ your_name

@app.route('/repeat/<int:num>/<string:anything>')
def repeat(num,anything):
    return f'{anything * num}'

@app.route('/play')
def play():
    return render_template("playground.html")

@app.route('/play/<int:x>/<string:background_color>')
def play1(x,background_color):
    return render_template("playground.html", num=x, c = background_color)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

# import statements, maybe some other routes
    