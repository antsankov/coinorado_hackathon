from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC2a9e06ea97e4a1a785361f0e8064e870"
auth_token  = "bc96d318cbda7ef495f1418baed042f4"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="7208378697",    # Replace with your phone number
    from_="7203300751") # Replace with your Twilio number
print message.sid