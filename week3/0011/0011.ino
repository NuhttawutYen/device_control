void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
  Serial.println("เมนู");
  Serial.println("1");
  Serial.println("2");
  Serial.println("3");
}

void loop() {
  if (Serial.available()) {
    char menu = Serial.read();

    if (menu == '1') Serial.println("ดีครรับ");
    else if (menu == '2') {
      Serial.print("ไม่เชื่อว่า  ");
      Serial.print(millis() / 1000);
      Serial.println(" วินาที");
    }
    else if (menu == '3') {
      Serial.print("สุ่มเอาละกัน ");
      Serial.println(random(1, 101));
    }
    else Serial.println("1-3เท่านั้นอย่าแหลม");
  }
}
