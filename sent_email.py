import smtplib, ssl

host = "smtp.gmail.com"
port = 465

user = "tylerskyler95@gmail.com"
password = "vwft atae kopz xvec"

receiver = "diego.cuellar.services@gmail.com"
context = ssl.create_default_context()

message = """ Hello, I hope you are doing well, this is just a test
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(user, password)
    server.sendmail(user, receiver, message)
