import os
import sys
import django
import datetime
from pathlib import Path
from twilio.rest import Client
from members.models import Member


project_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(project_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "church_registration.settings")

django.setup()

today = datetime.date.today()

members_with_birthday_today = Member.objects.filter(date_of_birth__day=today.day, date_of_birth__month=today.month)


# Your Twilio account credentials
account_sid = 'AC0a242acded83af93706c2f48ebc72ca9'
auth_token = '958f464a69f15db92bf9aadacf319d15'
client = Client(account_sid, auth_token)

for member in members_with_birthday_today:
    phone_number = member.phone_number
    message = f"Happy Birthday, {member.Other_name} {member.Surname}!"

    # Send WhatsApp message
    # client.messages.create(
    #     body=message,
    #     from_='whatsapp:your_twilio_whatsapp_number',
    #     to=f'whatsapp:{phone_number}',
    # )

    # Send SMS message
    client.messages.create(
        body=message,
        from_='your_twilio_sms_number',
        to=phone_number,
    )
