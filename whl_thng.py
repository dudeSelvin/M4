#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from twilio.rest import Client 
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 
#GPIO SETUP
channel = 8
channel2 = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(channel2, GPIO.IN)
 
def callback(channel):
    print("flame detected")
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='fire detected at 30.236640,-97.821456',      
                              to='whatsapp:+919344012834' 
                          ) 
 
GPIO.add_event_detect(channel, GPIO.FALLING, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
GPIO.add_event_detect(channel2, GPIO.FALLING, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel2, callback)
# infinite loop
while True:
        time.sleep(1)
