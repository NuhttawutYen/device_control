#include <ESP32Servo.h>
Servo myservo;
char user_input;

void setup() {
  Serial.begin(9600);
  myservo.attach(5);
  Servo();

}

void loop() {
  while (Serial.available() > 0) {
    char select_mode = Serial.read();
    user_input =  select_mode;

  if (user_input == '0') {
    Serial.println("Servo Motor => 90");
    myservo.write(90);
    delay(1000);
  }
  else if (user_input == '1') {  
    Serial.println("Servo Motor => 45");
    myservo.write(45);
    delay(1000);
  }
  else if (user_input == '3'){
    Serial.println("Servo Motor => 0");
    myservo.write(0);
    delay(1000);
  }
  else if (user_input == '4'){
    Serial.println("Servo Motor => 180");
    myservo.write(180);
    delay(1000);
    }
  }
}

