# visaEstimateEmailer
Script to email the current US Embassy wait time using Sendgrid

Currently placed on a Raspberry Pi Zero W with a daily Cronjob

Requires a 'secrets.cfg' file to provide a Sendgrid API key and an email account to receive the timestamped alert in the format:

[ClientSecrets]
api_key = <Your Sendgrid API key>
receiver_email = <Your email address>

