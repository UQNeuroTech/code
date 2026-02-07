/*

 - DO NOT PLUG LAPTOP INTO MAINS POWER WHILST RECORDING CAUSE IT MESSES UP THE SIGNAL
 - RED ON TOP OF BICEPT | YELLOW BOTTOM OF BICEPT | GREEN ON ELBOW


*/


#define PIN_LOPLUS 36
#define PIN_LOMINUS 39
#define PIN_OUTPUT 34

#define AVERAGE_SIZE 20
#define IGNORE_SIZE 10
#define THRESHOLD 300

#define PIN_LED 2

int baseline = 0;
int on = 0;
int iterations = 0;
int ignoring = 0;

void setup() {
  // initialize the serial communication:
  Serial.begin(9600);
  pinMode(PIN_LOPLUS, INPUT); // Setup for leads off detection LO +
  pinMode(PIN_LOMINUS, INPUT); // Setup for leads off detection LO -
  pinMode(PIN_LED, OUTPUT);

  delay(100);

  baseline = analogRead(PIN_OUTPUT);
}

void loop() {
  
  if((digitalRead(PIN_LOPLUS) == 1)||(digitalRead(PIN_LOPLUS) == 1)){
    Serial.println('!');
  }
  else{
    // send the value of analog input 0:
    int sum = 0;
    for (int i = 0; i <= AVERAGE_SIZE; i++) {
      sum += analogRead(PIN_OUTPUT);
      delay(3);
    }
    int average = sum / AVERAGE_SIZE;
    Serial.println(average);

    if ((average > baseline + THRESHOLD) && ignoring == 0) {
      if (on == 0) {
        digitalWrite(PIN_LED, HIGH);
        on = 1;
      } else {
        digitalWrite(PIN_LED, LOW);
        on = 0;
      }
      iterations = 0;
      ignoring = 1;
    }
  }
  //Wait for a bit to keep serial data from saturating
  delay(5);
  if (ignoring == 1) {
    iterations += 1;
    if (iterations >= IGNORE_SIZE) {
      ignoring = 0;
      iterations = 0;
    }
  }
}
