import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def send_mail(message = 'This is a test email.', recipient_email = 'martin.arthur.andersen@gmail.com', subject = 'Email from bot'):
    sender_email = 'bot@nettking.no'
    sender_name = 'Nettking Surveillance Bot'
    msg = MIMEText(message)
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = recipient_email
    msg['Subject'] = subject

    with smtplib.SMTP('smtp.proisp.no', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender_email, 'JabbaJabbaHei1990')
        smtp.sendmail(sender_email, recipient_email, msg.as_string())
        smtp.quit()