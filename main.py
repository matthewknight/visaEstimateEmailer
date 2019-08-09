import os
import requests
import configparser
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main():
    try:
        response = requests.get(
            'https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P17&aid=VisaWaitTimesHomePage')

        daysDelay = response.text.strip().split(",")[1].lower()
        timestampString = datetime.now().strftime('%Y/%m/%d %H:%M')

        config = configparser.ConfigParser()
        config.read('secret.cfg')

        emailUpdate = Mail(
            from_email='visaupdate@honeypi.com',
            to_emails=config.get('ClientSecrets', 'receiver_email'),
            subject='Visa Appointment Wait Times',
            html_content='Calendar day wait time: %s as of %s' % (daysDelay, timestampString)
        )

        sendGridClient = SendGridAPIClient(config.get('ClientSecrets', 'API_key'))
        response = sendGridClient.send(emailUpdate)
        if response.status_code == 202:
            print('Successfully sent email')
        else:
            print('Failed to send email, code: %s', response.status_code)
    except Exception as e:
        print(e)


main()
