import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail():
    message = MIMEMultipart()
    message['From'] = "ivfilippok@mail.ru"
    message['To'] = "ivfilippok@mail.ru"
    message['Subject'] = "Test report"
    text = "Test result"
    mypass = "fBCwfek3mFn3fR2uUsGH"
    message.attach(MIMEText(text))
    with open("log.txt", "rb") as f:
        attachment = MIMEApplication(f.read(), Name="log.txt")
        message.attach(attachment)

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(message['From'], mypass)
    text = message.as_string()
    server.sendmail(message['From'], message['To'], text)
    server.quit()
