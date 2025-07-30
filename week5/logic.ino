void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "ON") {
      digitalWrite(2, HIGH);
    }
    else if (command == "OFF") {
      digitalWrite(2, LOW);
    }
    else if (command == "BLIM") {
      blinkLED();
    }
  }
}

void blinkLED() {
  for (int i = 0; i < 5; i++) {
    digitalWrite(2, HIGH);
    delay(600);
    digitalWrite(2, LOW);
    delay(400);
  }
}

