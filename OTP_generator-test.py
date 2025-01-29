#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# In[2]:


import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to generate a 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP to the user's email address
def send_otp_via_email(recipient_email, otp):
    sender_email = "monir505085@gmail.com"  # Replace with your email address
    sender_password = "cype sxxb wtba hurp"  # Replace with your email password

    subject = "Your OTP Verification Code"
    body = f"Your OTP for verification is: {otp}"

    # Setting up the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        # Correct SMTP server for Gmail
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        print("OTP has been sent to your email.")
    except Exception as e:
        print("Failed to send OTP. Please check your email settings.", str(e))

# Function to prompt user for OTP and validate
def validate_otp(generated_otp):
    attempts = 3
    while attempts > 0:
        user_otp = input("Enter the OTP sent to your email: ")
        if user_otp == generated_otp:
            print("Access granted. OTP is correct!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect OTP. You have {attempts} attempts left.")
    print("Access denied. Too many incorrect attempts.")
    return False

if __name__ == "__main__":
    user_email = input("Enter your email address: ")
    otp = generate_otp()
    send_otp_via_email(user_email, otp)
    validate_otp(otp)



# In[ ]:




