import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from past.builtins import unicode

COMMASPACE = ', '
# Define params
rrdpath = '/home/osvaldo/Documents/redes/Introduccion_SNMP/6-AdministraciónDeRendimiento/RRD/'
imgpath = '/home/osvaldo/Documents/redes/Introduccion_SNMP/6-AdministraciónDeRendimiento/IMG/'
fname = 'Umbrales.rrd'

mailsender = "dummycuenta3@gmail.com"
mailreceip = "osvaldo.chavez9910@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'dvduuffmlhspbmjj'

def send_alert_attached(subject,i,info):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(imgpath+f'Rendimiento_CPU{i}.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    body = MIMEText(info, 'plain')
    msg.attach(body)
    msg.attach(img)
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()