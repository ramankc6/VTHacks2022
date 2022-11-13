from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from os import environ
import json
from twilio.rest import Client

with open("config.json", 'r') as env:
    environment = json.load(env)
    username = environment["user"]
    auth_token = environment["authToken"]


client = Client(username, auth_token)
app = Flask(__name__)
agent_phone = ['+15718355413']
twilioPhone = ['+17088477520']
cust_phone = ['+15717782230']


@app.route("/forward", methods=['GET','POST'])
def forward():
    incoming_message = request.form['Body']
    from_phone = request.form['From']
    print(from_phone)
    #count = 0
    #if(from_phone!= agent_phone and count==0):
        #cust_phone=from_phone
        #count+=1
        #ooga = client.messages.create(
         #   to = toPhone,
          #  from_= twilioPhone,
           # body=incoming_message)
    if(from_phone!='+15718355413'):
        ooga = client.messages.create(
            to = agent_phone,
            from_= twilioPhone,
            body=incoming_message)
    else:
        ooga = client.messages.create(
            to = cust_phone,
            from_= twilioPhone,
            body=incoming_message)
    return(ooga.sid)




   

if __name__ == '__main__':
    app.run(port=5002)