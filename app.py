#!/usr/bin/env python3
from flask import Flask, request, render_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    email = request.form["email"]
    Date = request.form["Date"]
    Persons = request.form["Persons"]

    send_email(email, name, Date, Persons)

    return "Reservering Ontvangen"

def send_email(email, name, Date, Persons):
    sender = os.environ["EMAIL_USER"]
    password = os.environ["EMAIL_PASS"]

    email_data = MIMEMultipart()
    email_data["From"] = sender
    email_data["To"] = email
    email_data["Subject"] = "Bevestiging reservering"

    body = f"Hallo Mr {name}, Dankuwel voor uw reservering op {Date} voor {Persons} personen. We kijken er naaruit u te zien.!"
    email_data.attach(MIMEText(body, "plain"))

    with smtplib.SMTPL("smtp.gmail.com", 587) as server:
      server.starttls()
      server.login(sender, password)
      server.sendmail(sender, email, email_data.as_string())

if __name__ == "__main__":
    app.run(debug=True)
