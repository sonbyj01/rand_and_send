# Rand[om] and Send 
Script written for [Yale CCM](https://www.yaleccm.org/) Daily Prayer Requests.

***Note: This only works for Gmail accounts. If you want to use another email provider, change the respective smtp address and port.***


## Synposis
- The script will randomly pick an email address from a list and send a message to that email. The objective is to maintain secrecy on who fills out the Google Form. 
- The cron tab script will send at the same time daily. I also add an error checking mechanism just in case the email fails the first time. 

## Requirements
No requirements are needed. All the libraries should already be installed. 

## Necessary Files
1. **'.credentials'**

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
2. **'emails.txt'**

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

## Running Program
```bash
# Running with 'python'
$ python3 rand_and_send.py

# Running as executable
$ chmod +x rand_and_send.py
$ ./rand_and_send.py
```

## Tasks at hand
- [x] send an email
- [x] randomly pick an email from list (waiting for the list...)
- [x] error checking just in case failed to connect to socket 
- [x] crontab script
- [ ] add other email domain smtp things
- [x] make a more comprehensive README.md