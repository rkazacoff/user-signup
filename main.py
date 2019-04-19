from flask import Flask, request
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
    <!DOCTYPE html>

    <html>
        <head>
            <link rel="stylesheet" href="/static/app.css" />
            
        </head>
        <body>
        <h1>Signup</h1>
    """

welcome_message = """
<h1>Welcome to my super cool page!</h1>
<a href="/register">Register</a> """


page_footer = """
       </body>
    </html>
    """

register_form = """
<form action="/register" id="form" method="POST">
    <h1>Register</h1>
    <label for="username">Username</label>
    <input type="text" name="username" id="username" value="{0}" />
    <p class="error">{1}</p>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" value="{2}" />
    <p class="error">{3}</p>
    <label for="password">Password Again</label>
    <input type="password" name="password2" id="password2" value="{4}" />
    <p class="error">{5}</p>
    <button type="submit">Register</button>
</form>
    """


@app.route("/", methods=['GET'])
def index():
    content = page_header + welcome_message + page_footer
    return content

@app.route("/register", methods=['POST'])
def register():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    password2 = cgi.escape(request.form['password2'])

    usernameError =""
    passwordError = ""
    password2Error =""

    if username == "":
        usernameError = 'Please enter a Username'
    if password == "":
        passwordError = 'Please enter a Username'        
    if password2 == "":
        password2Error = 'Please enter a Username'
    if len(username) < 3 or len(username) > 20:
        usernameError = 'Username must be between 3 and 20 characters'
        

    if usernameError or passwordError or password2Error:
        print("there was an error!")
        content = page_header + register_form.format(username, usernameError, 
        password, passwordError, password2, password2Error) + page_footer
        return content
   

    return "Thanks for registering, " + username

@app.route("/register", methods=['GET'])
def register_page():
    # build the response string
    content = page_header + register_form.format("", "", "", "", "", "") + page_footer
    return content



app.run()    