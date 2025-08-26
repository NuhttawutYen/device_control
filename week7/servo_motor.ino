#include <ESP32Servo.h>
Servo myservo;
char user_input;


void setup() {
  Serial.begin(9600);
  myservo.attach(22);
  Servo();
}

void loop() {
  while(Serial.available()> 0){
    char select_mode = Serial.read();
    user_input = char(Serial.read());

    if(user_input != select_mode){
      user_input = select_mode;
    }else{
      user_input = user_input;
    }
  }

  if(user_input == '0'){
    Serial.println('Servo Motor => 0 ');
    myservo.write(0);
    delay(1000);
  }else if(user_input == '1'){
    Serial.println('Servo Motor => 120 ');
    myservo.write(120);
    delay(1000);
  }else if(user_input == '2'){
    Serial.println('Servo Motor => 150 ');
    myservo.write(150);
    delay(1000);
  }else if(user_input == '3'){
    Serial.println('Servo Motor => 180 ');
    myservo.write(180);
    delay(1000);
  }else if(user_input == '4'){
    Serial.println('Servo Motor => 45 ');
    myservo.write(45);
    delay(1000);
  }

}