import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mailList = ["jufengwu102000@gmail.com","leowu102000@gmail.com"]

for rec in mailList:

    msg = MIMEMultipart()
    msg["From"] = "leowu102000@gmail.com"
    msg["To"] = rec
    msg["Subject"] = Header("Test send mail","utf-8").encode()
    msg_content = MIMEText("this is test")
    msg.attach(msg_content)
    ssl_context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
        server.login("leowu102000@gmail.com","uahy rbwi scfc uzen")
        server.sendmail("leowu102000@gmail.com",rec,msg.as_string())

        print("success send mail")