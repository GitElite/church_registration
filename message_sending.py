import os
import sys
import django
import pytz
from datetime import datetime
from twilio.rest import Client

# Add the path to your Django project
sys.path.append(os.path.abspath('./church_registration'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'church_registration.settings'
django.setup()

from django.conf import settings
from members.models import Member


def send_birthday_sms(phone_number, message):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    twilio_number = settings.TWILIO_PHONE_NUMBER

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=twilio_number,
        to=phone_number
    )

def send_whatsapp_birthday_message(phone_number, message):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    twilio_number = settings.TWILIO_PHONE_NUMBER

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_='whatsapp:twilio_number',
        to='whatsapp:+256775230160'
    )

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'church_registration.settings')

    try:
        django.setup()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


    now = datetime.now(pytz.timezone('Africa/Kampala'))
    
    if now.hour != 14:  # If it's not 00:00 (24-hour format), exit the script
        print("not right time")
        return

    today = now.date()

    members_with_birthday_today = Member.objects.filter(Date_of_birth__regex=r'-%02d-%02d$' % (today.month, today.day))

    for member in members_with_birthday_today:
        phone_number = member.Phone_number
        message = f"Happy Birthday, {member.Surname}! Wishing you a fantastic day!"
        send_birthday_sms(phone_number, message)
        send_whatsapp_birthday_message(phone_number, message)

if __name__ == '__main__':
    main()
