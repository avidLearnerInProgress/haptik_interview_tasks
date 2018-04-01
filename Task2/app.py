from flask import Flask, flash, redirect, render_template, request
from flask_restful import Resource, Api
import sqlite3
import hashlib
import datetime, json

app = Flask(__name__)
api = Api(app)
usrnm = ""

#----------------------Sqlite Connectivity-----------------------
c = sqlite3.connect("twitter.db", check_same_thread=False)
cursor = c.cursor()
c.execute('''CREATE TABLE If NOT EXISTS users
             (id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, username TEXT, email TEXT)''')

c.execute('''CREATE TABLE If NOT EXISTS tweets
             (id INTEGER PRIMARY KEY, tweet_id TEXT, tweet_content TEXT, created_at DATE, user_name TEXT)''')

#-----------------------Routes with templates---------------------
@app.route('/', methods=['GET'])
def user():
    return render_template('user.html')


@app.route('/', methods=['POST']) 
def user_post():
    fname = request.form['firstname']
    lname = request.form['lastname']
    global usrnm 
    usrnm = request.form['usrnm']
    email = request.form['email']
    flag = False

    users = c.execute("SELECT username from users")
    if usrnm in users:
        return render_template('user.html', flag = flag, data = "Username already exists")
    else:
        flag = True
        c.execute("INSERT INTO users (firstname, lastname, username, email) VALUES (?, ?, ?, ?)", (fname, lname, usrnm, email))
        return render_template('insert_tweet.html', flag = flag, usrnm = usrnm)


@app.route('/insert', methods=['GET','POST']) #insert tweet in database
def tweet():    
    content = request.form['tweet']
    global usrnm
    hash_content = content.encode()
    hash_object = hashlib.md5(hash_content)
    hex_dig = hash_object.hexdigest()
    timestamp = datetime.datetime.now()
    c.execute("INSERT INTO tweets (tweet_id, tweet_content, created_at, user_name) VALUES (?, ?, ?, ?)", (hex_dig, content, timestamp, usrnm))
    return render_template('insert_tweet.html', data = "Tweet Inserted Successfully")


@app.route("/tweets", methods=["GET", "POST"]) #get all tweets from database
def get_all_tweets():
    rows = c.execute("SELECT * FROM tweets ORDER BY id")
    all_tweets = []
    for row in rows:
        m = {}
        m = {'tweet_content' : row[2],'tweet_id' : row[1], 'timestamp' : row[3], 'user_name' : row[4]}
        all_tweets.append(m)
    return render_template("disp_tweet.html" , tweets = all_tweets)

@app.route("/users", methods=["GET", "POST"]) #get all users from database
def get_all_users():
    rows = c.execute("SELECT * FROM users ORDER BY id")
    all_users = []
    for row in rows:
        m = {}
        m = {'firstname' : row[1], 'lastname' : row[2], 'username' : row[3], 'email' : row[4]}
        all_users.append(m)
    return render_template("disp_user.html" , users = all_users)

#--------------Raw API Endpoints without templates----------------
class tweets_json(Resource):
    def get(self):
        rows = c.execute("SELECT * FROM tweets")
        json_list = []
        for ele in rows:
            m = {}
            m = {'id' : ele[0],'tweet_id' : ele[1], 'tweet' : ele[2], 'timestamp' : ele[3]}
            json_list.append(m)
        return json_list

class tweets_json_by_username(Resource):
    def get(self, uname):
        rows = c.execute("SELECT * FROM tweets WHERE user_name=? ORDER BY id",(uname,))
        json_list = []
        for ele in rows:
            m = {}
            m = {'id' : ele[0],'tweet_id' : ele[1], 'tweet' : ele[2], 'timestamp' : ele[3]}
            json_list.append(m)
        return json_list

api.add_resource(tweets_json, '/tweets/raw')
api.add_resource(tweets_json_by_username, '/tweets/<string:uname>')


if __name__ == '__main__':
    app.run(debug=True)
    c.commit()
    c.close()