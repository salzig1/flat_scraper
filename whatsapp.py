from twilio.rest import Client
from twilio_creds import auth_token, account_sid


client = Client(account_sid, auth_token)

def send_message(link):
    
    client.messages.create(
    from_='whatsapp:+14155238886',
    body=f"Neue Wohnung: {link}",
    to='whatsapp:+4915159122689'
    )


if __name__ == "__main__":
    send_message("link")