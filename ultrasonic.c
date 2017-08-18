#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
 
#define TRUE 1
 
#define TRIG 23
#define ECHO 18
 
void setup() {
        wiringPiSetup();
        pinMode(TRIG, OUTPUT);
        pinMode(ECHO, INPUT);
 
        //TRIG pin must start LOW
        digitalWrite(TRIG, LOW);
        delay(30);
}
 
int getCM() {
        //Send trig pulse
        digitalWrite(TRIG, HIGH);
        delayMicroseconds(20);
        digitalWrite(TRIG, LOW);
 
        //Wait for echo start
        while(digitalRead(ECHO) == LOW);
 
        //Wait for echo end
        long startTime = micros();
        while(digitalRead(ECHO) == HIGH);
        long travelTime = micros() - startTime;
 
        //Get distance in cm
        int distance = travelTime / 58;
 
        return distance;
}

int main(void) {
        setup();
    int i=0;
    char buffer [50];
    while (1)
    {
        int dist=getCM();
        printf("Distance: %dcm\n", dist);
        if ( dist<100) {
            i++;
            sprintf(buffer, "fswebcam -r 1280x720 snap%d.jpg",i);
            system(buffer);
            printf("gotcha!");
        }
    delay(1000);
    }
 
    return 0;
}

