import os
import time
import tweepy
consumer_key= 'JS7bbVBAo0j5ZDDMq5nJMVJV1'
consumer_secret= '7bTkI1c06sf8j2uDtRehCAkSQLuhUWACCLuG1FgKgrmImQODxM'
access_token= '967252071517970433-IsKl2YTxcjtUhE8LkFpXRXzcF6SNl3B'
access_token_secret= 'F3BAuVQfciu7EaSncW7T68WLXSIVROM78Y4G8lsVKg7xK'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)
b=1
a=0
while a<=2:
    img="/home/cs2017a106/Desktop/img"+str(b)+".jpg"
    cmd="fswebcam -r 1280x720 -S 3 --jpeg 100 "+img
    os.system(cmd)
    print("pic taken")
    api.update_with_media(img, status="lol")
    print("wait")
    time.sleep(3)
    a+=1
    b+=1
    print("done")
