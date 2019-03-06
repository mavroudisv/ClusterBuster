import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




def send_mail(job_id, job_name, status, timestamp):
	fromaddr = "YOUR EMAIL HERE"
	toaddr = "YOUR EMAIL HERE"
	
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "YOUR APP PASSWORD HERE") #https://myaccount.google.com/apppasswords
			
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Cluster Job Status Update (" + str(job_id) + ")"

	body = "<html><head></head><body><p> The cluster job <b>" + str(job_name) + "</b> (id: " + str(job_id) + ") is now in state <b>" + str(status) +"</b>.</p>"
	body += "</br>Time: <b>" + str(timestamp) + "</b></p></body></html>"

	msg.attach(MIMEText(body, 'html'))
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()


