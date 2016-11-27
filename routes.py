from flask import Flask, render_template, request
from models import db, User
from forms import SignupForm

'''
# Documentation
## This python file contains the controller of the application
## and it points to each of the html files that are found in 
## the ./templates folder. It does have some logic built in and
## in order to bring up the page it uses the render_template function
## that takes in the name of the html file.
'''

app = Flask(__name__)

# Connecting to postgresql database.  Needs a username and password in 
# this format -> username:password@localhost:5432/databasename
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tedo_admin:Oct1st!6@localhost:5432/learningflask'
db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.first_name.data,
                           form.last_name.data,
                           form.email.data,
                           form.password.data)
            db.session.add(newuser)
            db.session.commit()
            return "Success!"

    elif request.method == 'GET':
        return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
