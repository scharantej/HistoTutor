 
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Set the secret key for session management
app.secret_key = 'secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate the user credentials
        if username == 'admin' and password == 'secret':
            # Store the username in the session
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate the user input
        if username and password:
            # Create a new user account
            # Store the user data in the database
            return redirect(url_for('login'))
        else:
            return render_template('register.html', error='Please fill out all fields')
    else:
        return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/lessons')
def lessons():
    # Check if the user is logged in
    if 'username' in session:
        return render_template('lessons.html')
    else:
        return redirect(url_for('login'))

@app.route('/quizzes')
def quizzes():
    # Check if the user is logged in
    if 'username' in session:
        return render_template('quizzes.html')
    else:
        return redirect(url_for('login'))

@app.route('/resources')
def resources():
    # Check if the user is logged in
    if 'username' in session:
        return render_template('resources.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Clear the session and redirect to the home page
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
