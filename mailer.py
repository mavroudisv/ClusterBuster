import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import common as cm

def send_mail(job_id, job_name, status, timestamp):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(cm.EMAIL_FROM, cm.APP_PASSWORD)
			
	msg = MIMEMultipart()
	msg['From'] = cm.EMAIL_FROM
	msg['To'] = cm.EMAIL_TO
	msg['Subject'] = "Cluster Job Status Update (" + str(job_id) + ")"

	body = "<html><head></head><body><p> The cluster job <b>" + str(job_name) + "</b> (id: " + str(job_id) + ") is now in state <b>" + str(status) +"</b>.</p>"
	body += "</br>Time: <b>" + str(timestamp) + "</b></p></body></html>"

	msg.attach(MIMEText(body, 'html'))
	text = msg.as_string()
	server.sendmail(cm.EMAIL_FROM, cm.EMAIL_TO, text)
	server.quit()


