#include <ESP32Servo.h>
Servo myservo;
String  user_input;

void setup() {
  Serial.begin(9600);
  myservo.attach(22);
  Servo();
  pinMode(2, OUTPUT);
  
}

void loop() {
  if (Serial.available() > 0) {
    user_input = Serial.readStringUntil('\n');
    user_input.trim();
    



    if (user_input == "15") {
      Serial.println('Servo Motor => 15 ');
      myservo.write(15);
      blinkLED();
      delay(1000);

    } else if (user_input == "30") {
      Serial.println('Servo Motor => 30 ');
      myservo.write(30);
      blinkLED();
      delay(1000);
    } else if (user_input == "45") {
      Serial.println('Servo Motor => 45 ');
      myservo.write(45);
      blinkLED();
      delay(1000);
    } else if (user_input == "90") {
      Serial.println('Servo Motor => 90 ');
      myservo.write(90);
      digitalWrite(2, HIGH);
      delay(1000);
    } else if (user_input == "125") {
      Serial.println('Servo Motor => 125 ');
      myservo.write(125);
      blinkLED120();
      delay(1000);
      blinkLED();
    } else if (user_input == "135") {
      Serial.println('Servo Motor => 135 ');
      myservo.write(135);
      blinkLED120();
      delay(1000);
    } else if (user_input == "150") {
      Serial.println('Servo Motor => 150 ');
      myservo.write(150);
      blinkLED120();
      delay(1000);
    } else if (user_input == "stop") {
      Serial.println('Servo Motor => 0 ');
      myservo.write(0);
      digitalWrite(2, LOW);
      delay(1000);
    }
  }
}

void blinkLED() {
  for (int i = 0; i < 2; i++) {
    digitalWrite(2, HIGH);
    delay(1000);
    digitalWrite(2, LOW);
    delay(1000);
  }
}

void blinkLED120() {
  for (int i = 0; i < 5; i++) {
    digitalWrite(2, HIGH);
    delay(2000);
    digitalWrite(2, LOW);
    delay(2000);
  }
}