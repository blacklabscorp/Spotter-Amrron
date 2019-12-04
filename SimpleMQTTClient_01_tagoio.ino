/*
  SimpleMQTTClient.ino
  The purpose of this exemple is to illustrate a simple handling of MQTT and Wifi connection.
  Once it connects successfully to a Wifi network and a MQTT broker, it subscribe to a topic and send a message to it.
  It will also send a message delayed 5 seconds later.
*/

#include "SparkFunBME280.h"
BME280 bme;
#include "EspMQTTClient.h"

EspMQTTClient client(
  "Bear2Mixed",
  "xxxxxxx",
  "3.92.246.6",  // MQTT Broker server ip
  "xxxxxxxxxxx",   // Can be omitted if not needed
  "xxxxxxxxxxx",   // Can be omitted if not needed
  "romeo07",     // Client name that uniquely identify your device
  1883              // The MQTT port, default to 1883. this line can be omitted
);
float temperature[8];
void setup()
{
  Serial.begin(115200);

  Wire.begin();
  if (bme.beginI2C() == false) //Begin communication over I2C
  {
    Serial.println("The sensor did not respond. Please check wiring.");
    while(1); //Freeze
  };
}


void onConnectionEstablished()
{
//  client.publish("amrron/CA", "This is a message"); // You can activate the retain flag by setting the third parameter to true
}

void loop()
{
float temperature = bme.readTempF(); 
// Convert the value to a char array
char tempString[8];
dtostrf(temperature, 1, 2, tempString);
client.publish("tago/data/post",("{"temperature:",tempString}");
Serial.print("Temperature: ");
Serial.println(tempString);



  Serial.print(" Temp: ");
  //Serial.print(bme.readTempC(), 2);
    Serial.print(bme.readTempF(), 2);
  Serial.println();

  delay(10000);
  client.loop();
}
