const int pinTemp = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
//   Serial.println("530");
//   delay(1000);
//   Serial.println("531");
//   delay(1000);
//   Serial.println("533");
//  delay(1000);
//  Serial.println("533");
//  delay(1000);
//  Serial.println("533");
//  delay(1000);
//  Serial.println("530");
//  delay(1000);
//  Serial.println("531");
//  delay(1000);
//  Serial.println("533");
//  delay(1000);
//  Serial.println("533");
//  delay(1000);
//  Serial.println("533");
//  delay(1000);
//  Serial.println("530");
//  delay(1000);
//  Serial.println("531");
//  delay(1000);
//  Serial.println("533");
//  delay(1000);
//  Serial.println("533");
//  delay(1000);
//  Serial.println("539");
//  delay(1000);
//  // Para combrar que no explote con un valor distinto de un número
//  Serial.println("Hola jejeplot"); 
//  delay(1000);

  int temp_reading = analogRead(pinTemp);
  Serial.println(temp_reading);
  delay(1000);
}
