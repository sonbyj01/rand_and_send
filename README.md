# Rand[om] and Send 
Script written for Yale CCM Daily Prayer Requests

***This only works for Gmail accounts. If you want to use another email provider, change the respective 
smtp address and port.***

The script will randomly pick an email from a list and send a Google Form link to that email. 
The objective is to maintain secrecy on who fills out the Google Form. A cron tab script will be created
soon so it will send at the same time daily. I will also add an error checking mechanism just in case
the email fails the first time. 

## Using this script
### '.credentials'
Create a '.credentials' file within the same directory as the script, which should contain the following information:
```
{{ email address }} 
{{ password }}
```
So for example, 
```
test@domain.com
password1234567890
```
### 'emails.txt'
Create a text file that contains the list of email addresses you want to choose from. New line for each email address.
```
{{ email1@domain.com }}
{{ email2@domain.com }}
{{ email3@domain.com }}
```
So for example, 
```
test1@gmail.com
test2@yahoo.com
test3@hotmail.com
```

## Tasks at hand
- [x] send an email
- [x] randomly pick an email from list (waiting for the list...)
- [x] error checking just in case failed to connect to socket 
- [x] crontab script
- [ ] make a more comprehensive README.md