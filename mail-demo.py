import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
toaddr = 'david@localhost'

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
# with smtplib.SMTP('localhost', 1025) as smtp:
    #smtp.ehlo()
    #smtp.starttls()
    #smtp.ehlo()

    #smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

subject = 'Test email from python'
body = 'This is only a test!'

msg = f'Subject: {subject}\n\n{body}'

# smtp.sendmail(EMAIL_ADDRESS, 'david@localhost', msg)

server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(1)
server.sendmail(EMAIL_ADDRESS, toaddr, msg)
server.quit()
