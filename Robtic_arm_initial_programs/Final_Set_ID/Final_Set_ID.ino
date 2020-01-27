#include "AX12A.h"

#define DirectionPin   (10u)
#define BaudRate      (1000000ul)
#define ID        (2u)

void setup() {
  delay(100);
  ax12a.begin(BaudRate, DirectionPin, &Serial);
  ax12a.setID(ID,4);
}
 
void loop() {
 
 
}
