<img src="./logo.png">

# ClusterBuster
ClusterBuster: Monitors your cluster jobs and sends you an email when they change state

##Requirements
-Python 3.6

## Setup
1. Create a gmail account to send the emails from. 
2. Generate an application password from: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Edit ''mailer.py'' and include: your email, the email address to send notifications to, and your newly generated password.
4. Edit you username for the cluster machine in ''monitoring.py''.
5. From the ''monitoring.py'' script you can edit for how long the script will keep looking for new jobs (STOP_AFTER).


## Instructions
Run ```python monitoring.py```

That's all. If you want to close the terminal you can also do 

```nohup python3 monitoring.py &```
