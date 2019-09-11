import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import password


sender_email = 'ms0094449@gmail.com'
Reciver_email = 'ms0094449@gmail.com'
password = password.password
subject = 'fyp Report'
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = Reciver_email
msg['Subject'] = subject

message ='suspect found please be carefull'
msg.attach(MIMEText(message,'plain'))
filename='messi.jpg'
attachment=open(filename,'rb')

part = MIMEBase('application','octet_stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('content-Disposition',"attachment; filename= "+filename)
msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ms0094449@gmail.com',password)
server.sendmail(sender_email,Reciver_email,text)
server.quit()