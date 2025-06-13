from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Cambialo in produzione
app.permanent_session_lifetime = timedelta(minutes=30)

# Carica utenti da file JSON
with open('users.json') as f:
    users = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session.permanent = True
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Credenziali non valide', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=8200)
