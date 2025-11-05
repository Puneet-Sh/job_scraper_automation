import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_report(sender, password, receiver, report_path):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = "Automated Job Report"

    body = "Attached is the latest job report."
    msg.attach(MIMEText(body, 'plain'))

    with open(report_path, 'rb') as f:
        msg.attach(MIMEText(f.read(), 'csv'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
