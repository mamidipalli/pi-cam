#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_2.py
# Measure distance using an ultrasonic module
# in a loop.
#
# Author : Matt Hawkins
# Date   : 28/01/2013

# -----------------------
# Import required Python libraries
# -----------------------
import time
import RPi.GPIO as GPIO

# -----------------------
# Define some functions
# -----------------------

def measure():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  # print "Ultrasonic Measurement y1"
  time.sleep(0.00001)
  # print "Ultrasonic Measurement y2"
  GPIO.output(GPIO_TRIGGER, False)
  # print "Ultrasonic Measurement y3"
  start = time.time()
  # print "Ultrasonic Measurement y4"

  while GPIO.input(GPIO_ECHO)==0:
    # print "Ultrasonic Measurement y5"
    start = time.time()
    # print "Ultrasonic Measurement y6"
  print GPIO.input(GPIO_ECHO)
  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()
    # print "Ultrasonic Measurement y7"

  # print "Ultrasonic Measurement y8"
  elapsed = stop-start
  # print "Ultrasonic Measurement y9"
  distance = (elapsed * 34300)/2
  # print "Ultrasonic Measurement y10"  

  return distance

def measure_average():
  # This function takes 3 measurements and
  # returns the average.
  distance1=measure()
  # print "Ultrasonic Measurement x1"
  time.sleep(0.1)
  # print "Ultrasonic Measurement x2"
  distance2=measure()
  # print "Ultrasonic Measurement x3"
  time.sleep(0.1)
  # print "Ultrasonic Measurement x4"
  distance3=measure()
  # print "Ultrasonic Measurement x5"
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 4
GPIO_ECHO    = 17

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
# print "Ultrasonic Measurement 1"
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
# print "Ultrasonic Measurement 2"

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)
# print "Ultrasonic Measurement 3"

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:
  # print "Ultrasonic Measurement 4"
  while True:
    # print "Ultrasonic Measurement 5"
    distance = measure_average()
    # print "Distance : %.1f" % distance
    time.sleep(1)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()

