from time import sleep
import subprocess
import time
import sys
from datetime import datetime
from mailer import send_mail

import common as cm


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
		jobs[details[0]]=(details[2],details[4]) #key: id, value: (name, state)
	return jobs

	
	
##############################################################################################
jobs = {}
inactive_rounds = 0

while True:
	sleep(cm.INTERVAL) #Start the day after a good night sleep.
	new_jobs = check_jobs(cm.USERNAME)
	
	#Stop looking for a job if it's finished.
	to_remove = []	
	for j in jobs:
		if j not in new_jobs:
			event_state_change(j,jobs[j][0],"finished")
			to_remove.append(j)
	for i in to_remove:
		del jobs[i]
	
	#If there are no new jobs. Go back to sleep.
	if new_jobs == {}:
		inactive_rounds += 1
		continue

	#There are jobs to monitor for
	inactive_rounds = 0
	to_add = {}
	for j in new_jobs:
		if not (j in jobs):
			to_add[j]=new_jobs[j]
			event_state_change(j,new_jobs[j][0],new_jobs[j][1])
		elif (j in jobs) and (jobs[j][1]!=new_jobs[j][1]):
			jobs[j]=new_jobs[j]
			event_state_change(j,new_jobs[j][0],new_jobs[j][1])
	for i in to_add:
		jobs[i] = new_jobs[j]
	
	
	#Exit if we haven't seen any jobs in a while
	if inactive_rounds > cm.STOP_AFTER:
		sys.exit(0)