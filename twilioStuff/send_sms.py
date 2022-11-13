from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9a7dc846c75614072af080adf179816e"
# Your Auth Token from twilio.com/console
auth_token  = "56120522a3125fe2a08acafc0de4ea28"

client = Client(account_sid, auth_token)

contact = input("Who this going to? ")

message = input("Say sum: ")




message = client.messages.create(
    to=contact, 
    from_="+17088477520",
    body=message)

print(message.sid)