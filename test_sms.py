from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'AC0a242acded83af93706c2f48ebc72ca9'
auth_token = '958f464a69f15db92bf9aadacf319d15'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Replace 'your_twilio_number' with your Twilio phone number
# Replace 'recipient_phone_number' with the recipient's phone number
message = client.messages.create(
    body="Hello, this is a scheduled test SMS message!",
    from_='+16204136355',
    to='+256775230160'
)

print(f"Message sent! Message SID: {message.sid}")
