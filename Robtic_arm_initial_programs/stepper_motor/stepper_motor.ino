#include "AX12A.h"
#include <Stepper.h>
#include <Servo.h>


#define DirectionPin   (10u)
#define BaudRate      (1000000ul)
#define ID        (1u)
#define STEPS 2038

Stepper stepper(STEPS, 8, 10, 9, 11);
Servo myservo1,myservo2;  

long int get_id(long int incoming_data_value){
    while(incoming_data_value >= 10){
      incoming_data_value = incoming_data_value/10;
      }
    return incoming_data_value;
  }
long int get_angle(long int incoming_data_value){
      long int length_of_number=1;
      long int temp = incoming_data_value;
      while(incoming_data_value >= 10){
        incoming_data_value = incoming_data_value/10;
        length_of_number = length_of_number * 10;
        }
      return temp%length_of_number;
   }

String incomingByte_ID ;    
long int angle_value;
long int ID_number;
long int temp2;
long int direction_stepper;

void setup() {
  Serial.begin(BaudRate);
  ax12a.begin(BaudRate, DirectionPin, &Serial);
  stepper.setSpeed(5);
  myservo1.attach(9);
  myservo2.attach(11);
}

void loop() {
  if(Serial.available()>0){
      incomingByte_ID = Serial.readStringUntil('\n');
      temp2 = incomingByte_ID.toInt();
      ID_number = get_id(temp2);
      angle_value = get_angle(temp2);

      if(ID_number == 1){
            direction_stepper = get_id(angle_value);
            if(direction_stepper == 1){
                Serial.print(" Steper Motor ID: 4     Direction : Positive    angle : ");
                angle_value = get_angle(angle_value);
                Serial.println(angle_value);
                stepper.step(angle_value);
                
              }else if(direction_stepper == 2){
                Serial.print(" Steper Motor ID: 4     Direction : Negative    angle : ");
                angle_value = get_angle(angle_value);
                Serial.println(angle_value);
                stepper.step((-1)*angle_value);
            }
        }
      if(ID_number == 2){
          ax12a.setMaxTorque(1,1000);
          ax12a.moveSpeed(2,angle_value,60);
          Serial.print("   ID =  2   ");
          Serial.print("set angle = ");
          Serial.println(angle_value);
        }
      if(ID_number == 3){
          ax12a.setMaxTorque(1,1000);
          ax12a.moveSpeed(3,angle_value,60);
          Serial.print("   ID =  3   ");
          Serial.print("set angle = ");
          Serial.println(angle_value);
        }
      if(ID_number == 4){
          ax12a.setMaxTorque(1,1000);
          ax12a.moveSpeed(4,angle_value,60);
          Serial.print("   ID =  4  ");
           Serial.print("set angle = ");
          Serial.println(angle_value);
        }

        if(ID_number == 5){
              // micro servo 1
              Serial.print(" Micro servo ID : 5     angle : ");
              myservo1.write(angle_value);
              Serial.println(angle_value);
          }
        if(ID_number == 6){
              // mmicro servo 2
              Serial.print(" Micro servo ID : 5     angle : ");
              myservo2.write(angle_value);
              Serial.println(angle_value);
          }
        
    }
}
