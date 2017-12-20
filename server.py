from flask import Flask, render_template
import sqlite3 as lite

app = Flask(__name__)

con = None
try:
    con = lite.connect('donald.db')
except lite.Error as e:
    pass


@app.route('/')
def index():
    context = {}
    cur = con.cursor()
    cur.execute('SELECT text, img FROM Tweets LIMIT 5;')
    tweets = cur.fetchall()
    [
            (text, link),(),()
            ]
    print(tweets)
    context['tweets'] = tweets
    return render_template('index.html', **context)
