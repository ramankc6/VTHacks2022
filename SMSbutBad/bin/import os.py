import os
from twilio.rest import Client


account_sid = "AC9a7dc846c75614072af080adf179816e"
auth_token  = "56120522a3125fe2a08acafc0de4ea28"




message = client.messages().fetch()

print(message.to)
    
