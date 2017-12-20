import twitter
import json
import sqlite3 as lite
import sys

api = twitter.Api(consumer_key='3aOfW5zQJNkwCvBlGDGLAsro9',
        consumer_secret='zrAAcWgz5RqFgejOf5I7dRhvayZKcSnNdCunwOtKUzc4XgYEFR',
        access_token_key='943599484201824256-Ehs6Z52T3sKZWo7YimPzp9SUOnmThO3',
        access_token_secret='alkCpobxCy2dki8iIK1GkXCHldaVDEGLmybo0BULEdWOl')

con = None
try:
    con = lite.connect('donald.db')
except lite.Error as e:
    pass

statuses = api.GetUserTimeline(screen_name='realDonaldTrump', count=200, include_rts=False)
cur = con.cursor()
for status in statuses:
    print(status)
    cur.execute("INSERT into Tweets(text) VALUES (?);", (status.text,))
    
con.commit()
con.close()
print('done')
