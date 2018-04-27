from flask import Flask, request, redirect, render_template, flash
import os
import string


app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'fadj9qbitrgqn4oqtrenfa8j4o3q'

email_verification ='@'
period_verification = '.'
@app.route('/')
def new_route():
    return redirect ('/signup')

@app.route('/signup', methods=['POST' , 'GET'])
def signup():
    username =""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        if len(username) < 2:
            flash('Must enter a unique username longer than 3 characters', 'error')
            return render_template ('indexhome.html')
        if len(password) < 2:
            flash('Must enter a password longer than 3 characters', 'error')
            return render_template ('indexhome.html',username=username, email=email)
        #if username or password (string.whitespace):
            #flash('Check Username or Password for spaces','error')
        
        if password != verify:
            flash('Check your verification for typos!','error')
            return render_template ('indexhome.html',username=username, email=email)
        if email != "" and (email_verification) and (period_verification) not in email:
            flash ('Enter valid email with @ and a period!','error')
            return render_template ('indexhome.html',username=username, email=email)
        
        else:
            return redirect ('/welcome?username={0}'.format(username)) 
    else:
        return render_template ('indexhome.html')
        

@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcomepage.html', username=username)

app.run()