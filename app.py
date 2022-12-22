from flask import Flask, request, render_template

# Create a new Flask app instance
app = Flask(__name__)

# A list of valid users for the login form
users = [
    {'username': 'user1', 'password': 'pass1'},
    {'username': 'user2', 'password': 'pass2'},
    {'username': 'user3', 'password': 'pass3'},
]

@app.route('/login', methods=['POST'])
def login():
    # Get the form data
    username = request.form['username']
    password = request.form['password']
    
    # Check if the form data matches a valid user
    for user in users:
        if user['username'] == username and user['password'] == password:
            # If the login is successful, render the dashboard template
            return render_template('dashboard.html')
        else: 
            # If the login is unsuccessful, redirect back to the login page popup with message 
            return render_template('index.html', message="Invalid username or password")
    return render_template('index.html', message="Invalid username or password")

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")
