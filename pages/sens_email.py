import smtplib, ssl

host = "mail.bkt.birosag.hu"
port = 25

username = "mailadmin@"
password = "passwiord str"

receiver = "mailadmin@bkt.birosag.hu"
context = ""

message = """
Hi!
How are you?
Bye!
"""

with smtplib.SMTP(host, port) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)