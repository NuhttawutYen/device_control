void setup() {
 Serial.begin(9600);
 pinMode(2, OUTPUT);

}

void loop() {
  //เช็ค com port
  if(Serial.available()){
    String command = Serial.readStringUntil('\n');
    command.trim();

    if(command == "ON"){
      digitalWrite(2,1);

    }
    else if (command == "OFF") {
      digitalWrite(2, 0);
   
    }
    else if ( command == "BLINK") {
      blinkLED();
    }
  }
}


void blinkLED(){
  for (int i =0; i< 5; i++){
    digitalWrite(2, 1);
    delay(400);
    digitalWrite(2, 0);
    delay(400);
  }
}