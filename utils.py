import os
import smtplib
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS_2')
EMAIL_PASSWORD = os.environ.get('APP_PASSWORD_2')


def mail(to: str, content: str):
    """Send Email to recipients"""

    msg = EmailMessage()
    msg['Subject'] = 'Xray Analysis Report'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to

    msg.set_content(content)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


if __name__ == "__main__":

    try:
        mail(to="ajaykrish.krishnanrb@gmail.com", content="test")
        print('Mail send')
    except:
        print('Error Sending mail')
