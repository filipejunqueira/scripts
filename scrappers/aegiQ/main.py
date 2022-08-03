from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import xlwt
import os
from docx import Document
import pickle
from progressbar import ProgressBar

URL = r"https://www.aegiq.com/"
message = 'We currently don\'t have open positions, but feel free to send us a message at jobs@aegiq.com'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
# jobs_check = soup.find("div", attrs={"id": "comp-keu6rmfc"}).text
jobs_check = 'The p element is not the same at https://www.aegiq.com/!'

# email section:

subject = 'AEGIQ WEBSITE HAS CHANGED!!!'
text = """Hi, The p element is not the same at aegiq https://www.aegiq.com/!"""
html = """"\
<html>
  <body>
    <p>Hi,<br>
       The p element is not the same at aegiq:</p>
    <p><a href="https://www.aegiq.com/"> AegiQ website</a></p>
  </body>
</html>
"""


#email parameters:
port = 587
smtp_server = "smtp.gmail.com"
user = "mybroccolibot@gmail.com"
p = "rlenifdssjhnubco"

sender_email = "mybroccolibot@gmail.com"
receiver_email = "filipelqj@gmail.com"

# message

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# convert both parts to MIMEText objects and add them to the MIMEMultipart message
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# send your email
with smtplib.SMTP_SSL(smtp_server, port) as server:
    try:
        server.ehlo()
        server.login(user, p)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    except:
        print("something went wrong")

# the check
if message != jobs_check:
    print("something changed!")
    # creating server

else:
    print("everything is the same")
    pass
