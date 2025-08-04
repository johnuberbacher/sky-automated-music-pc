#include <Keyboard.h>

void setup() {
  Serial.begin(9600);
  Keyboard.begin();
}

void loop() {
  if (Serial.available() > 0) {
    char input = Serial.read();

    Keyboard.press(input);
    delay(50);
    Keyboard.release(input);
  }
}
