import RPi.GPIO as GPIO 
import time 
#GPIO SETUP 
channel = 21 
GPIO. setmode (GPIO. BCM) 
GPIO. setup (channel, GPIO. .IN) 
def callback (channel) : 
        if GPIO. input (channel): 
            print("no water detected") 
        else: 
            print ("water detected"} 
GPI0.add_event_detect (channel, GPIO. BOTH, bouncetime=300) # let us know when the pin goes HIGH or LOW 
GP10.add_event_callback (channel, callback) 
                                             # assign function to - GPIO PIN, Run function on change 
# infinite loop 
while True: 
        time.sleep (1)
