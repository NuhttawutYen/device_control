#include "DHT.h"

#define DHTPIN 4        
#define DHTTYPE DHT11   

DHT dht(DHTPIN, DHTTYPE);  

void setup() {
  Serial.begin(9600); 
  dht.begin();         
}

void loop() {
  float temp = dht.readTemperature();   
  float hum = dht.readHumidity();       

  if (!isnan(temp) && !isnan(hum)) {    
    Serial.print("Temp: ");
    Serial.print("Temp");
    Serial.print("hum");            
    Serial.print("Hum");

  } else {
    Serial.println("");
  }

  delay(2000); 
}
