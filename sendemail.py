import smtplib

HOST = "smtp.mydomain.com"
PORT = 587
SUBJECT = "Test email from Python"
TO = "ronokipcollins@gmail.com"
FROM = "ronocollins2000@gmail.com"
EMAIL_HOST_PASSWORD = "xsduljzwtwbtrqpn"
text = "blah blah blah"
BODY = "\r\n".join((
    f"From: {FROM}",
    f"To: {TO}",
    f"Subject: {SUBJECT}",
    "",
    text
))
server = smtplib.SMTP(HOST, PORT)
server.sendmail(FROM, [TO], BODY)
server.quit()