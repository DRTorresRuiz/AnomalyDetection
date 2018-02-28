const int pinTemp = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int temp_reading = analogRead(pinTemp);
  Serial.println(temp_reading);
  delay(1000);
}
