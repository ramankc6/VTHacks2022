import os
import csv
import json
from twilio.rest import Client
from collections import Counter

#securing username and pass
with open("config.json", 'r') as env:
    environment = json.load(env)
    username = environment["user"]
    auth_token = environment["authToken"]

#Twilio Authorization
client = Client(username, auth_token)

#get 10 last messages
messages = client.messages.list(limit=10, to=+17088477520)

bigList = []


for record in messages:

    #get body of message and set all to lower
    plswork = client.messages(record.sid).fetch()
    message = plswork.body
    message = message.lower()
    #print(message)
    words = list(message.split())
    print(words)
    i=0
    size = len(words)

    #Iterate through words and add to larger list

    while(i<size):
        bigList.append(words[i])
        i+=1
#print(bigList)

#
freq = Counter(bigList)
print(freq)

#Write Count to CSV
f = open('myfile.csv', 'w')
with open('myfile.csv', 'w') as f:
    writer = csv.writer(f)
    f.write('Word , Freq\n')  
    for tag, count in freq.items():  
        f.write('{},{}\n'.format(tag, count))
f.close()
        
 

