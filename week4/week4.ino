const int greenLed = 8;
const int redLed = 9;

int countdownSeconds = 0;
bool isOn = false;
bool readyToStart = false;

void setup() {
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);

  Serial.begin(9600);
  Serial.println("ใส่จำนวนวินาทีเพื่อเปิดไฟเขียว:");
}

void loop() {
  if (Serial.available() > 0) {
    countdownSeconds = Serial.parseInt(); // รับค่าจาก Serial
    if (countdownSeconds > 0) {
      readyToStart = true;
    } else {
      Serial.println("กรุณาใส่เลขมากกว่า 0");
    }
  }

  if (readyToStart && !isOn) {
    // เตรียมตัว
    Serial.println("Ready...");
    delay(1000);
    Serial.println("Set...");
    delay(1000);
    Serial.println("Go!");
    delay(500);

    // เปิดไฟเขียว
    digitalWrite(greenLed, HIGH);
    digitalWrite(redLed, LOW);
    isOn = true;
    Serial.println("ไฟเขียว ON");

    for (int i = countdownSeconds; i > 0; i--) {
      Serial.print("Light Green - ");
      Serial.println(i);
      delay(1000);
    }

    //เปลี่ยนเป็นไฟแดง
    digitalWrite(greenLed, LOW);
    digitalWrite(redLed, HIGH);
    Serial.println("หมดเวลาไฟเขียว → เปลี่ยนเป็นไฟแดง");
    Serial.println("off");

    delay(3000); // ไฟแดงค้าง 3 วินาที
    digitalWrite(redLed, LOW);

    isOn = false;
    readyToStart = false;
    Serial.println("ใส่จำนวนวินาทีเพื่อเปิดไฟเขียว:");
  }
}




