import boto
import boto.s3
import sys, os, glob, time
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import requests
import io
import urllib
#import tinys3
from PIL import Image
from boto.s3.key import Key 
from gpiozero import DistanceSensor
from picamera import PiCamera
from datetime import datetime
ultrasonic = DistanceSensor(echo=17, trigger=4)
ultrasonic.distance

camera = PiCamera()

AWS_ACCESS = 'AKIAJFDNGSITR26VKKTQ'
AWS_SECRET = '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'

#conn = tinys3. Connection(AWS_ACCESS,AWS_SECRET,tls=True)
#bucket = conn.get_bucket('rekognition-usecases')
#directory = '/tmp/'

def captureImage():
    print("log2") 
    camera.capture('/tmp/picampic1.png')
    print("Image Captured")
    upload()

def upload():
    print("log3")
    conn = tinys3. Connection(AWS_ACCESS,AWS_SECRET,tls=True)
    f=open('/tmp/picampic1.png','rb')
    conn.upload('/tmp/picampic1.png',f,'rekognition-usecases')
    print("uploaded")
   

while True:
    print("log1")
    ultrasonic.when_in_range = captureImage
    time.sleep(8)
    print("log4")

   
 
