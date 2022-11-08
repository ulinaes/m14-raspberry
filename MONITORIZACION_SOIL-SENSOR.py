#!/usr/bin/python
# Importar librerias necesarias:
import RPi.GPIO as GPIO
import time
import httplib, urllib
import urllib2
import json

# Activar GPIO mode:
GPIO.setmode(GPIO.BCM)

# Define El pin GPIO de salida de información:
channel = 17
GPIO.setup(channel, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# Indica chat de slack donde se envia
webhook_url = "https://hooks.slack.com/services/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"
def postToSlack():
    data = '{"attachments":[{"fallback":"Water plant!","pretext":"The soil is too dry!","color":"#cc0000","fields":[{"title":"The Garden Room plant needs watering!","short":false}]}]}'
    slack = urllib2.Request(webhook_url, data, {'Content-Type': 'application/json'})
    post = urllib2.urlopen(slack)
    post.close()

# Recibe señales del sensor en bucle y envia notificaciones
while True:
    if GPIO.input(channel)==False:
        #print('Suelo esta humedo')
        time.sleep(900)
    else:
        #print('Suelo esta seco')
        postToSlack()
        time.sleep(2700)
