import smtplib, ssl

def send_mail(message, receiver,):
    host = "mail.bkt.birosag.hu"
    port = 25

    username = "mailadmin"
    password = "Onenetvision1."

    receiver = "sandorsz@birosag.hu"
    context = ""

    with smtplib.SMTP(host, port) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)