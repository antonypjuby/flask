from flask import Blueprint,render_template,request,flash
auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
       data= request.form
       return render_template("login.html",boolean =True)

@auth.route('/logout')
def logout():
       return "<p>logout</p>"

@auth.route('/signup')
def signup():
       return render_template("signup.html",methods=['GET','POST'])

