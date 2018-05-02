int val = 0;
int photoresistor_pin = 5; //might change pin for photoresistor wiring
void setup() {
  //set serial monitor bit rate to 9600
  Serial.begin(9600);
}

void loop() {
  //save photoresitor valuse to photoresistor output
  val = analogRead(photoresistor_pin);
  Serial.println(val); //print values on new line
}
