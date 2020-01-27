#include "AX12A.h"

#define DirectionPin   (10u)
#define BaudRate      (1000000ul)
#define ID        (1u)

String incomingByte_ID,incomingByte_angle ;    

void setup() {

  Serial.begin(BaudRate);
  ax12a.begin(BaudRate, DirectionPin, &Serial);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

  while(Serial.available() == 0) {
  }
  incomingByte_ID = Serial.readStringUntil('\n');
  
  while(Serial.available() == 0) {
  }
  incomingByte_angle = Serial.readStringUntil('\n');
  
  ax12a.move(incomingByte_ID.toInt(), incomingByte_angle.toInt());
  delay(200);
}
