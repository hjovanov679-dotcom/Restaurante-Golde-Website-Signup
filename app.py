#!/usr/bin/env python3
from flask import Flask, request, render_template
import requests
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
    api_key = os.environ["RESEND_API_KEY"]

    headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"}

    body = {
      "from": "reserveringen@restaurante-golde.nl",
      "to": email,
      "subject": "Bevestiging reservering",
      "text": ( 
        f"Hallo {name}!\n\n"
        f"Bedankt voor u reservering bij Restaurante Golde op {Date} voor {Persons} personen.\n\n"
        "We kijken er naar uit u te zien!\n\n\n"
        "Restaurante Golde, het luxste restaurant van heel de benelux!"
      )
}  
    response = requests.post(
    "https://api.resend.com/emails",
    headers=headers,
    json=body)

if __name__ == "__main__":
    app.run(debug=True)
