from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC9a7dc846c75614072af080adf179816e"
# Your Auth Token from twilio.com/console
auth_token  = "56120522a3125fe2a08acafc0de4ea28"
client = Client(account_sid, auth_token)

app = Flask(__name__)
@app.route("/forward", methods=['GET','POST'])

agent_phone = ['+15718355413']
customer_phone = ['']

def reply(message, recipient):
    response = MessagingResponse()
    response.message(body=message, to=recipient)
    
    print(message)
  
    ooga = client.messages.create(
       
        to = "+recipient",
        from_="+17088477520",
        body=message
    )
    return str(response)


def forward():
    global current_customer
    incoming_message = request.form['Body']
    from_phone = request.form['From']

    if (from_phone == agent_phone): # message came from agent
         reply(f'Agent: {incoming_message}', current_customer)
    else: # message came from a customer
            reply(incoming_message, from_phone)
            return reply(f'{current_customer}: {incoming_message}',
                agent_phone)
    

if __name__ == "__main__":
    app.run(port=5002)