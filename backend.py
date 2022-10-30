from flask import Flask,redirect,url_for,render_template,request,session,flash
#from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://user.sqlite3"
#app.permanent_session_lifetime(minutes=30)

#db = SQLAlchemy(app)

#class users(db.Model):
#    _id = db.Column("id",db.Integer,primary_key=True)


@app.route("/")
def home():
    return render_template("onlyerrors.html")

@app.route("/login")
def login():
#        return render_template("dashboard.html")
        return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/aboutus")
def about():
    return render_template("aboutus.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.pop("user",None)
    return render_template("onlyerrors.html")

if __name__ == "__main__":
    app.run(debug=True)