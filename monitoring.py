from time import sleep
import subprocess
import time
import sys
from datetime import datetime

from mailer import send_mail

#Settings
USERNAME = 'YOUR USERNAME'
INTERVAL = 6
STOP_AFTER = 600 #If not job is detected for STOP_AFTER intervals exit.
 
 
#Measurements
submitted_at = 0
started_at   = 0
finished_at  = 0

 
 
##Submit job
#process = subprocess.Popen(['qsub', 'job.sh'], stdout=subprocess.PIPE)
#out, err = process.communicate()

#Get id
#id = str(out).split(" ")[2]

#jobs[id] = {state}
#Query jobs
#if new id shows up -> event: new job
#if existing job 	-> event: state change


def event_state_change(id,name,current_state):
	stamp = datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	send_mail(id,name,current_state,stamp) #Send email

def check_jobs(uname):
	jobs = {} #id, (name, status)
	process = subprocess.Popen(['qstat', '-u',  uname], stdout=subprocess.PIPE)
	out, err = process.communicate()
	out = out.decode("utf-8")
	for row in out.splitlines()[2:]:
		details = row.split()
		jobs[details[0]]=(details[2],details[4])
	return jobs

	
	
##############################################################################################
jobs = {}

inactive_rounds = 0
while True:
	sleep(INTERVAL)
	new_jobs = check_jobs(USERNAME)
	
	if new_jobs == {}:
		inactive_rounds += 1
		continue
	else:
		for j in new_jobs:
			if not j in jobs:
				jobs[j]=new_jobs[j]
				event_state_change(j,new_jobs[j][0],new_jobs[j][1])
			elif j in jobs and (jobs[j]!=new_jobs[j]):
				jobs[j]=new_jobs[j]
				event_state_change(j,new_jobs[j][0],new_jobs[j][1])
	to_remove = []	
	for j in jobs:
		if j not in new_jobs:
			event_state_change(j,jobs[j][0],"finished")
			to_remove.append(j)
	
	for i in to_remove:
		del jobs[i]