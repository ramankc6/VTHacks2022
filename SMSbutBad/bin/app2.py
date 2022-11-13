from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from os import environ
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC9a7dc846c75614072af080adf179816e"
# Your Auth Token from twilio.com/console
auth_token  = "56120522a3125fe2a08acafc0de4ea28"

client = Client(account_sid, auth_token)
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

print("yo momma")


   

if __name__ == '__main__':
    app.run(port=5002)