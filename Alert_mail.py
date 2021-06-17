import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("<email>","<password>")
message= """\
Subject: Mlops-Project ALERT !!!

There is some issue while launching the container."""
s.sendmail("<sender_mail>","<receiver_mail>",message)
s.quit()
