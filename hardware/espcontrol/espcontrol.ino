#include <WiFi.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

#include <ESP32Servo.h>
 
Servo myservo;  // create servo object to control a servo
// 16 servo objects can be created on the ESP32
 
int pos = 0;    // variable to store the servo position
// Recommended PWM GPIO pins on the ESP32 include 2,4,12-19,21-23,25-27,32-33 
int servoPin = 23;


const int buttonPin = 2;
const char* ssid = "ib-701";
const char* password =  "d07c66cd58";
int buttonState = 0;
WiFiServer wifiServer(80);
LiquidCrystal_I2C lcd(0x27,20,4);

void buka(){
   // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);    // tell servo to go to position in variable 'pos'
    delay(15);             // waits 15ms for the servo to reach the position
  }             // waits 15ms for the servo to reach the position
  
  }

void tutup(){
   // goes from 180 degrees to 0 degrees
    myservo.write(180);    // tell servo to go to position in variable 'pos'
    delay(15);             // waits 15ms for the servo to reach the position
  
  }
void setup() {
    // Allow allocation of all timers
  ESP32PWM::allocateTimer(0);
  ESP32PWM::allocateTimer(1);
  ESP32PWM::allocateTimer(2);
  ESP32PWM::allocateTimer(3);
  myservo.setPeriodHertz(50);    // standard 50 hz servo
  myservo.attach(servoPin, 500, 2400);
  
  pinMode(buttonPin, INPUT);
  Serial.begin(115200);
  lcd.init();                      // initialize the lcd 
  lcd.init();
  // Print a message to the LCD.
  lcd.backlight();
  delay(1000);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }

  Serial.println("Connected to the WiFi network");
  Serial.println(WiFi.localIP());

  wifiServer.begin();
}

void loop() {
  lcd.setCursor(0,0);
  lcd.print("connecting");
  WiFiClient client = wifiServer.available();

  if (client) {

    while (client.connected()) {
        lcd.setCursor(0,0);
        lcd.print("Press a button");
        buttonState = digitalRead(buttonPin);
        if (buttonState == HIGH) {
          client.write("1");
          Serial.println("1");
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("wait....");
        }
        else{
          client.write("0");
          Serial.println("0");
          }
        while (client.available()>0) {
        char c = client.read();
          
          buka();
          delay(1000);
          
      }
      tutup();
        lcd.clear();
      delay(10);
    }
      
    client.stop();
    Serial.println("Client disconnected");

  }
}
