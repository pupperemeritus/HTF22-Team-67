from flask import Flask,redirect,url_for,render_template,request,session,flash
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://user.sqlite3"
app = Flask(__name__)
app.permanent_session_lifetime(minutes=30)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id",db.Integer,primary_key=True)
    

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["GET", "POST"])
def login():
    if session.method == "POST":
        session.permanent = True
        user = request.form["Username"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user",usr=user))
        return render_template("login.html")

@app.route("/signup",methods=["GET", "POST"])
def signup():
    if session.method == "POST":
        if request.form["Password"] == 
        session.permanent = True
        user = request.form["Username"]
        session["user"] = user
        return redirect(url_for("user"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)