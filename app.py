from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import json
from main import Susbot
import pandas as pd

with open("config.json", 'r') as env:
    environment = json.load(env)
    username = environment["user"]
    auth_token = environment["authToken"]

client = Client(username, auth_token)
companyPhone = ['+14793481227']

app = Flask(__name__)
@app.route("/forward", methods=['GET','POST'])

def forward():
    Surbot = False
    incoming_message = request.form['Body']
    from_phone = request.form['From']
    if(Surbot == True):
        
        ooga = client.messages.create(
            to = from_phone,
            from_= companyPhone,
            body= Susbot(incoming_message)
        )
    elif(incoming_message == "Susbot"):
        Surbot=True
        ooga = client.messages.create(
            to = from_phone,
            from_= companyPhone,
            body="Enter in this order\nModel Year:  Make:  \nModel:  Fuel Type(X for regular, Z for premium, D for diesel, E for electric")
            
    
    else:
        ooga = client.messages.create(
            to = from_phone,
            from_= companyPhone,
            body="Type \"Susbot\" to calculate!")
    


    

if __name__ == "__main__":
    app.run(port=5004)