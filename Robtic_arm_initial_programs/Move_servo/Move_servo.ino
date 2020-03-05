#include "AX12A.h"

#define DirectionPin   (10u)
#define BaudRate      (1000000ul)
#define ID        (1u)

String incomingByte_ID ;    
int angle_value;
void setup() {
  Serial.begin(BaudRate);
  ax12a.begin(BaudRate, DirectionPin, &Serial);
}

void loop() {
  if(Serial.available()>0){
      incomingByte_ID = Serial.readStringUntil('\n');
      
      if(incomingByte_ID.toInt()/1000 == 1){
          
          angle_value = incomingByte_ID.toInt()-1000;
          ax12a.setMaxTorque(1,1000);
          ax12a.moveSpeed(1,angle_value,100);
          Serial.print("   ID =  1   ");
          Serial.print("set angle = ");
          Serial.println(incomingByte_ID.toInt()-1000);
        }
      if(incomingByte_ID.toInt()/1000 == 2){
        
          angle_value = incomingByte_ID.toInt()-2000;
          ax12a.setMaxTorque(2,1000);
          ax12a.moveSpeed(2,angle_value,60);
          Serial.print("   ID =  2   ");
          Serial.print("set angle = ");
          Serial.println(incomingByte_ID.toInt()-2000);
        }
      if(incomingByte_ID.toInt()/1000 == 3){
          
          angle_value = incomingByte_ID.toInt()-3000;
          ax12a.setMaxTorque(3,1000);
          ax12a.moveSpeed(3,angle_value,60);
          Serial.print("   ID =  3   ");
          Serial.print("set angle = ");
          Serial.println(incomingByte_ID.toInt()-3000);
        }
      if(incomingByte_ID.toInt()/1000 == 4){
          
          angle_value = incomingByte_ID.toInt()-4000;
          ax12a.setMaxTorque(4,1000);
          ax12a.moveSpeed(4,angle_value,60);
          Serial.print("   ID =  4   ");
          Serial.print("set angle = ");
          Serial.println(incomingByte_ID.toInt()-4000);
        }
    }
}
