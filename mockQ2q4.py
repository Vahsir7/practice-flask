from flask import Flask, request, url_for, redirect

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return 'This is the dashboard'

@app.route('/user/<username>')
def user(username):
    return f'This is {username} profile'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return url_for('user', username='your_name')
    else:
        return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
