from flask import Flask, render_template
from flask_login import LoginManager




#Initializing the app
app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#Creating and intilaizing login manager
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def hello():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()