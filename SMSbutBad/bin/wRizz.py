import os
import csv
import json
from twilio.rest import Client
from collections import Counter

with open("config.json", 'r') as env:
    environment = json.load(env)
    username = environment["user"]
    auth_token = environment["authToken"]


client = Client(username, auth_token)
#client = Client('AC9a7dc846c75614072af080adf179816e','56120522a3125fe2a08acafc0de4ea28')

messages = client.messages.list(limit=10, to=+17088477520)


bigList = []
for record in messages:
    #message = client.messages(record.sid).fetch()
    #print(message.to)
    #print(record.sid)print(client.messages(record.sid).fetch())
    plswork = client.messages(record.sid).fetch()
    message = plswork.body
    message = message.lower()
    #print(message)
    words = list(message.split())
    print(words)
    i=0
    size = len(words)
    while(i<size):
        bigList.append(words[i])
        i+=1
#print(bigList)

freq = Counter(bigList)
print(freq)


f = open('myfile.csv', 'w')
with open('myfile.csv', 'w') as f:
    writer = csv.writer(f)
    f.write('Word|Freq\n')  
    for tag, count in freq.items():  
        f.write('{}|{}\n'.format(tag, count))
f.close()
        
 

