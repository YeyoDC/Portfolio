import smtplib, ssl
import os


def send_email(message, receiver):
    host = "smtp.gmail.com"
    port = 465
    user = "tylerskyler95@gmail.com"
    # This is to set up the environment variable, so we can have confidential information
    password = os.getenv("PASSWORD")
    context = ssl.create_default_context()

    #  this is to send the email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user, password)
        server.sendmail(user, receiver, message)

