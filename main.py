 
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def home():
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
    if username == 'admin' and password == 'secret':
      session['logged_in'] = True
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
    if username == 'admin' and password == 'secret':
      return render_template('register.html', error='Username already exists')
    else:
      session['logged_in'] = True
      return redirect(url_for('dashboard'))
  else:
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
  if 'logged_in' in session:
    return render_template('dashboard.html')
  else:
    return redirect(url_for('login'))

@app.route('/lessons')
def lessons():
  if 'logged_in' in session:
    return render_template('lessons.html')
  else:
    return redirect(url_for('login'))

@app.route('/quizzes')
def quizzes():
  if 'logged_in' in session:
    return render_template('quizzes.html')
  else:
    return redirect(url_for('login'))

@app.route('/resources')
def resources():
  if 'logged_in' in session:
    return render_template('resources.html')
  else:
    return redirect(url_for('login'))

if __name__ == '__main__':
  app.run(debug=True)
