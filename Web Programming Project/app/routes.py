from asyncio.windows_events import NULL
from pprint import pprint
from flask import render_template, flash, redirect, url_for
from sqlalchemy import null
from app import app
from flask import request
from app.models import Login1
from app import db
import pymongo

#mongodb sample data
client = pymongo.MongoClient("mongodb+srv://Nithin:12345@cluster0.3mubmvh.mongodb.net/?retryWrites=true&w=majority")
mongoDB = client.sample_restaurants
neighcol= mongoDB.neighborhood
restaurantscol= mongoDB.restaurants

global username1;username1= NULL
global resturant1; resturant1= NULL
@app.route('/',methods=['GET'])
@app.route('/login',methods=['GET'])

def login():
    return render_template('login.html')

@app.route('/',methods=['POST'])
@app.route('/login',methods=['POST'])
def post_login():
        if request.form['action']=='SignUp':
            return redirect('/registration')
        else:
            globals().update(username1=request.form.get("username","<missing username>"))
            password1=request.form.get("password","<missing password>")
            print(username1)
            u1=0
            u=Login1.query.filter(Login1.username==username1)
            
            for u in u:
                print(u.username)
            try:
                if u.username==username1 :
                    if u.password==password1:
                        return redirect('/index')
                    else:
                        return '<html><h1>login failed</h1></html>'
                else:
                        return '<html><h1>login failed</h1></html>'
            except :
                return '<html<p>user not exists</p></html>'
            
            

                
@app.route("/registration",methods=['GET'])
def register():
    return render_template('registration.html',status=1)

@app.route("/registration",methods=['POST'])
def post_register():
    username1=request.form.get("username","<missing username")
    password1=request.form.get("password","<missing password>")
    confirm_password1=request.form.get("confirm_password","<missing confirm_password>")
    print(password1)
    print(confirm_password1)
    if password1 == confirm_password1:
        u=Login1(username=username1,password=password1)
        db.session.add(u)
        try:
            db.session.commit()
            submitted=1
        except :
            db.session.rollback()
            submitted=0
        return render_template('registration.html',submitted=submitted,status=0)
    else:
        return '<html><h1>password and confirm password does not match</h1> <br><br><a href="/index"> HOME</a> </html>'
@app.route('/index',methods=['GET'])
def login_1(): 
    cities = fetchCity()
    return render_template('index.html',username=username1,city=cities)

@app.route("/restaurant",methods=['POST'])
def fetchRestaurantsByCity():

    restaurants=[]
    city = request.form.get('city')
    for r in list(restaurantscol.find({}).limit(150)):
        if city==r['borough']:
            restaurants.append(r)
    return render_template('index.html',city=fetchCity(),restaurant=restaurants,username=username1)


def fetchCity():
    city=set()
    for r in list(restaurantscol.find({}).limit(150)):
        city.add(r['borough'])
    return city



