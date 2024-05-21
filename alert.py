from twilio.rest import Client

account_sid = '[account_sid]'
auth_token = '[auth_token]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',         # Twilio phone number
  body='Appointment is now available!',  # Message
  to='whatsapp:+92xxxxxxxxxx'            # Your phone number  
)

print(message.sid)