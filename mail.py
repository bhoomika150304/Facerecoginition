
####################################################################

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

######################################################################



def report_send_mail(subject, body_, user_id):

            fromaddr = "mdraf657@gmail.com"
            toaddr = user_id
               
            # instance of MIMEMultipart 
            msg = MIMEMultipart() 
              
            # storing the senders email address   
            msg['From'] = fromaddr 
              
            # storing the receivers email address  
            msg['To'] = toaddr 
              
            # storing the subject  
            msg['Subject'] = subject
              
            # string to store the body of the mail 
            body = body_



            part = MIMEBase('application', "octet-stream")
            part.set_payload(open("data.xlsx", "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="data.xlsx"')
            msg.attach(part)
              
            # attach the body with the msg instance 
            msg.attach(MIMEText(body, 'plain')) 
              
              
            # creates SMTP session 
            s = smtplib.SMTP('smtp.gmail.com', 587) 
              
            # start TLS for security 
            s.starttls() 
              
            # Authentication 
            s.login(fromaddr, "Afgh456j") 
              
            # Converts the Multipart msg into a string 
            text = msg.as_string() 
              
            # sending the mail 
            s.sendmail(fromaddr, toaddr, text) 
              
            # terminating the session 
            s.quit() 



 
