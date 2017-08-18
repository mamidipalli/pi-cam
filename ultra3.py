from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=17, trigger=4)
ultrasonic.distance
while True:
    print(ultrasonic.distance)
