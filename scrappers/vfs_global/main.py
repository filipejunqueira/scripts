import smtplib, ssl
import requests
import time
#import tensorflow as tf

from scrapper_lib import SCRAPPER

status = "404"
apppass = "yvjuofdtyytzjrzu"
message = []


for i in range(1,5):
    url_tnt = "https://delivery.tnt.com/consignment-svc/api/v1/consignments/tracking?postcode=NG24NXi&consignmentNumber=100739194&pan="
    message = requests.get(url = url_tnt, timeout=5.00)
    status = message.status_code
    print(f"{i} message {status}")
    time.sleep(3)


