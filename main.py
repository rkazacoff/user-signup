from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route("/")

def index():
    return render_template('entry_form.html')


@app.route("/register", methods=['POST'])
def register():
    
   # return render_template('entry_form.html')
    
    usernameError =""
    emailError =""
    passwordError = ""
    password2Error =""
    user_space = ''
       
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    password2 = request.form['password2']

    print(username, password)
    if not username:
        usernameError = 'Please enter a Username'
        
    elif user_space == '':
        for x in username:
            if x == ' ':
                usernameError = 'Username must not contain spaces'
        for x in password:
            if x == ' ':
                passwordError = 'Password must not contain spaces'
        
    if len(username) < 3 or len(username) > 20:
        usernameError = 'Username must be between 3 and 20 characters'

    if email != "" and len(email) < 3 or len(email) > 20:
        emailError = 'Not a valid email'
    elif email != "" and ("." not in email or "@" not in email):
        emailError = 'Not a valid email'

    if password == "":
        passwordError = 'Please enter a Password'        
    
    elif password2 == "":
        password2Error = 'Please confirm your Password'
        
    
    elif password != password2:
        passwordError = 'Your passwords must match!'

    if usernameError or emailError or passwordError or password2Error:
        return render_template('entry_form.html', username=username, usernameError=usernameError, 
        passwordError=passwordError, password2Error=password2Error, email=email, emailError=emailError)
        

    return render_template('greeting.html', username=username, 
    usernameError=usernameError, passwordError=passwordError,
    password2Error=password2Error, email=email, emailError=emailError)

app.run()    