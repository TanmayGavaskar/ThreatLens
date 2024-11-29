# Importing all the libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.chrome.service import Service
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Functions
def send_email(recipient):
    try:
        # Create a MIMEMultipart object to represent the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")


# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = ('nachiketmarkale7@gmail.com')  # Replace with your email or use an environment variable
sender_password = ('dlew riwg bluq yeky')  # Replace with your password or use an environment variable
subject = 'Critical/High Vulnerabilities'
recipient_email = 'tanay013rahulkar@gmail.com'  # Replace with recipient's email


#Invoking the website
path = "D:\\Nachiket\\Study\\SIH_2024\\chromedrivcer.exe"
service = Service(path)
driver = webdriver.Chrome() 
driver.get("https://sec.cloudapps.cisco.com/security/center/publicationListing.x")
driver.fullscreen_window()
time.sleep(5)

in_loop = driver.find_element(By.XPATH , f"//body[1]/cdc-template[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[2]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[4]").text
checkdate = datetime.today().strftime('%Y %b %d')
i = 0


for i in range(1 , 21):
    a=[]
    for j in range(1 , 6):
        impact = driver.find_element(By.XPATH , f"//body[1]/cdc-template[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[2]/tr[{i}]/td[1]/table[1]/tbody[1]/tr[1]/td[2]").text
        dt = driver.find_element(By.XPATH , f"//body[1]/cdc-template[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[2]/tr[{i}]/td[1]/table[1]/tbody[1]/tr[1]/td[4]").text
        
        if impact == "High" or impact == "Critical":
            txt = driver.find_element(By.XPATH , f"//body[1]/cdc-template[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[2]/tr[{i}]/td[1]/table[1]/tbody[1]/tr[1]/td[{j}]").text
            a.append(txt)
            print(txt + "\t")

    i+=1
    print("\n")

    #Sending email
    if a != []:
        result = "\n".join(a)
        body = result
        send_email(recipient_email)