<p align="center">
	<img src="./images/logo.png" width="500" height="500">
</p>

# ClusterBuster
Monitors your cluster jobs and sends you an email when they change state.

### Features
* No mailserver is required.
* Each job has its own conversation thread in Gmail.
* Returns the process logs of each finished job.
* Monitoring process exits after <user-defined> hours of inactity.

## Requirements
* Python 3.6

## Setup
1. Create a gmail account to send the emails from. 
2. Generate an application password from: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Edit ''common.py'' and include: your gmail address, the email address to send notifications to, your username for the cluster machine, and your newly generated password.
4. Optionally, you can edit ''common.py'' to set for how long the script will keep looking for new jobs (STOP_AFTER).


## Instructions
Run: ```python monitoring.py```

That's all. If you want to close the terminal you can also do:

```nohup python monitoring.py >/dev/null 2>&1 &```

This will run the monitoring in the background, will supress any nohup output files, and will keep running even if you end your session.
