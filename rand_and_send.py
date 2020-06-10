#!/usr/bin/env python3

import smtplib
import ssl
import random
import pickle
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class RandAndSend:
    def __init__(self, addresses_text):
        # loads existing pickle file that contains updated list of addresses to choose from
        # otherwise create a new list of addresses from text file specified
        try:
            with open('data.pickle', 'rb') as f:
                self.data = pickle.load(f)
                print(self.data)f
        except FileNotFoundError as fnf:
            print(fnf)
            self.data = []
            with open(addresses_text, 'r') as f:
                content = f.readlines()
                self.data = [x.strip() for x in content]

    def run(self):
        self._send(self._select())
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.data, f)

    def _select(self):
        try:
            random_number = random.randint(0, len(self.data) - 1)
            return self.data.pop(random_number)
        except (IndexError, ValueError) as err:
            print(err)
            exit()

    def _send(self, to_email):
        try:
            with open('.credentials', 'r') as f:
                self.from_email = f.readline()
                self.from_password = f.readline()
        except FileNotFoundError as fnf:
            print(fnf)
            exit()

        self.from_port = 465  # SSL

        # set up email packet
        self.message = MIMEMultipart('alternative')
        self.message['Subject'] = 'Daily Prayer Request'
        self.message['From'] = 'Prayer Request'
        self.message['To'] = to_email

        # set up message
        self.text = """\
        Hey you, today's your day!
        Fill the Google Form for tonight's prayer: 
        https://forms.gle/blahblahblah
        """

        self.part = MIMEText(self.text, 'plain')
        self.message.attach(self.part)

        # create a secure SSL context
        self.context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', self.from_port, context=self.context) as server:
                server.login(self.from_email, self.from_password)
                server.sendmail(self.from_email, to_email, self.message.as_string())
        except:
            time.sleep(5)
            self._send(to_email)


def main():
    RandAndSend('emails.txt').run()


if __name__ == '__main__':
    main()
