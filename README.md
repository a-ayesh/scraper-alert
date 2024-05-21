# Appointment Availability Checker

This script periodically checks the appointment availability for any application website (be it for a course at your uni, or a visa appointment at the embassy). This example checks for student applications at the German Consulate in Islamabad. When an appointment is available, it sends an alert via WhatsApp using Twilio.

## Installation

1. Clone the repository (if applicable) or download the script files.
2. Install the required packages:
```sh
pip install requests beautifulsoup4 twilio
```
3. Set up Twilio:
    - Sign up at Twilio.
    - Get your Account SID and Auth Token from the Twilio console.
    - Obtain a Twilio phone number enabled for WhatsApp.

## Configuration
1. Update Twilio credentials:
    Replace [account_sid] and [auth_token] with your Twilio Account SID and Auth Token in the script.

2. Set the WhatsApp number to get alerts on:
    Replace 'whatsapp:+92xxxxxxxxxx' with your phone number in WhatsApp format.

## Usage 
1. Run the script:
```sh
python appointment_checker.py
```
2. The script will:
    - Periodically check the specified webpage for availability.
    - Parse the webpage to find specific keywords related to applications.
    - If an appointment is found, it will run a separate alert script (alert.py) 30 times.
    - Send an alert message via WhatsApp.