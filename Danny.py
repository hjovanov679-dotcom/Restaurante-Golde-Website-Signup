#!/usr/bin/env python3
def signup():
    name = request.form["name"]
    name = request.form["email"]
    name = request.form["Date"]
    name = request.form["Persons"]

def data(name = input(name_signup), email = input(email_signup), date = input(date_signup), persons = input(persons_signup)):
    send_email(email, name, Date, Persons)

def send_email(email, name):
    sender = hjovanov679@gmail.com
    password = tzma mcwv pksk xurk

email_data = MIMEMultipart
body = "Hallo Mr ", name, "Dankuwel voor uw reservering op ", Date, "voor", Persons, "Persons. We kijken er naaruit u te zien.!"
email_data.attach(MIMEtext(body, plain))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, email, email_data.as_string())