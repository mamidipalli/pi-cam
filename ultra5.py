import boto
import boto.s3
import sys, os, glob, time
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import requests
import io
#from StringIO import StringIO
import urllib
from PIL import Image
from boto.s3.key import Key 
from gpiozero import DistanceSensor
from picamera import PiCamera
from datetime import datetime
from random import randint
ultrasonic = DistanceSensor(echo=17, trigger=4)
ultrasonic.distance
i=0
camera = PiCamera()
#datetime = datetime.now().isoformat()
AWS_ACCESS = 'AKIAJFDNGSITR26VKKTQ'
AWS_SECRET = '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'
conn = S3Connection(AWS_ACCESS,AWS_SECRET)
bucket = conn.get_bucket('search-faces-rekognition')
directory = '/tmp/'
lastCaptureTime = time.time()

#def captureImage1():
#    if imgCnt<2
#    	captureImage1()
#        imgCnt++

def captureImage():
    #datetime = datetime.now().isoformat()
    #camera.capture('/tmp/%s.jpg' %datetime)
    rand=randint(1000000,99999999)
    print("log2") 
    curTime = time.time()
    elapsedTime = curTime - lastCaptureTime
    print("e Time :%s "%elapsedTime)
    camera.capture('/tmp/%s.jpg' %rand  ) 
    #camera.close() 
    print("Image Captured")
    #camera.led = False
    #lastCaptureTime = time.time() 
    
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def getFiles(dir):
        return [os.path.basename(x) for x in glob.glob(str(dir) + '*.jpg')]


def upload_S3(dir, file):
        k = Key(bucket)
        k.key = f
 #      setPinHigh()
        k.set_contents_from_filename(dir + f, cb=percent_cb, num_cb=10)
 #      setPinLow()
        #lastCaptureTime = time.time()

def removeLocal(dir, file):
        os.remove(dir + file)
        #camera.led = False

while True :
    #ultrasonic.wait_for_in_range()
    #print("In range")
    #ultrasonic.wait_for_out_of_range()
    #print("Out of range")
     print("log1")
     ultrasonic.when_in_range = captureImage
     print("log to capture image3")
     time.sleep(10)
     filenames = getFiles(directory)
     print("log for file directory")
     for f in filenames:
          #print 'rnUploading %s to Amazon S3 bucket %s' % (f, bucket)
           print ('uploading')
           upload_S3(directory,f)
           removeLocal(directory,f)
#     time.sleep(30)
