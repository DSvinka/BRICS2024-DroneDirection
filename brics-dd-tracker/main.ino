#include "Servo.h"

Servo rightServo;
Servo leftServo;
Servo topServo;
Servo downServo;

void setup() {
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  Serial.begin(115200);
  rightServo.attach( 5,  500,  2500);
  rightServo.write(115); //115

  leftServo.attach(6, 500, 2500);
  leftServo.write(90); // 95

  topServo.attach(10, 500, 2500);
  topServo.write(12);

}
uint8_t angle2 = 15; 

uint16_t topSignal = 0;
uint16_t bottomSignal = 0;
uint16_t rightSignal = 0;

void loop() {
  rightSignal = analogRead(2);
  topSignal = analogRead(0);
  bottomSignal = analogRead(1);

    
    Serial.print(rightSignal);
    Serial.print(" ");
    Serial.print(topSignal);
    Serial.print(" ");
    Serial.println(bottomSignal);

    if(topSignal > 60 || bottomSignal > 60) {
      if (bottomSignal - topSignal > 2) {
        if(angle2<60) {
          angle2+=1;
        }
        
        
        topServo.write(angle2);
      }
    
      if (topSignal - bottomSignal > 2){
        if(angle2 > 15) {
          angle2 -= 1;
        }
        topServo.write(angle2);
      }
    }


  delay(5);
}