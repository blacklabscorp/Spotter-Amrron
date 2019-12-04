#include "SparkFunCCS811.h"
#include "Wire.h"
#include "Sparkfun_APDS9301_Library.h"
#include "SparkFunBME280.h"
BME280 bme;
#include "EspMQTTClient.h"
CCS811 ccs(0x5B);
APDS9301 apds;

// Pin assignment definitions
#define WIND_SPD_PIN 14
#define RAIN_PIN     25
#define WIND_DIR_PIN 35
#define AIR_RST      4
#define AIR_WAKE     15
#define DONE_LED     5




EspMQTTClient client(
  "Bear2Mixed",
  "xxxxx",
  "192.168.1.200",  // MQTT Broker server ip
  "MQTTUsername",   // Can be omitted if not needed
  "MQTTPassword",   // Can be omitted if not needed
  "Romeo07",     // Client name that uniquely identify your device
  1883              // The MQTT port, default to 1883. this line can be omitted
);
float temperature[8];
float humidity[8];
float barometer[8];
float altitude[8];

void setup()
{
  Serial.begin(115200);

  Wire.begin();
  if (bme.beginI2C() == false) //Begin communication over I2C
  {
    Serial.println("The sensor did not respond. Please check wiring.");
    while(1); //Freeze
  };

  bme.settings.commInterface = I2C_MODE;
  bme.settings.I2CAddress = 0x77;
  bme.settings.runMode = 3;
  bme.settings.tStandby = 0;
  bme.settings.filter = 0;
  bme.settings.tempOverSample = 1;
  bme.settings.pressOverSample = 1;
  bme.settings.humidOverSample = 1;
  bme.begin();

  // CCS811 sensor setup.
  pinMode(AIR_WAKE, OUTPUT);
  digitalWrite(AIR_WAKE, LOW);
  pinMode(AIR_RST, OUTPUT);
  digitalWrite(AIR_RST, LOW);
  delay(10);
  digitalWrite(AIR_RST, HIGH);
  delay(100);
  ccs.begin();

  // APDS9301 sensor setup. Leave the default settings in place.
  apds.begin(0x39);
}

void onConnectionEstablished()
{
}

void loop()
{
float temperature = ((bme.readTempF())-9); 
float humidity = ((bme.readFloatHumidity())+10);
float barometer = bme.readFloatPressure();
float altitude = bme.readFloatAltitudeFeet();
float co2 = ccs.getCO2();
float tvoc = ccs.getTVOC();
float lux = apds.readLuxLevel();

// Trigger the CCS811's internal update procedure, then
    //  dump the values to the serial port.
    ccs.readAlgorithmResults();

// Convert the value to a char array
char tempString[8];
dtostrf(temperature, 1, 2, tempString);
Serial.print("Temperature: ");
Serial.println(tempString);
client.publish("amrron/romeo07/temperature", tempString);

// Convert the value to a char array
char humString[8];
dtostrf(humidity, 1, 2, humString);
Serial.print("Humidity: ");
Serial.println(humString);
client.publish("amrron/romeo07/humidity", humString);

// Convert the value to a char array
char baroString[8];
dtostrf(barometer, 0, 0, baroString);
Serial.print("Barometric: ");
Serial.println(baroString);
client.publish("amrron/romeo07/barometer", baroString);

// Convert the value to a char array
char altString[8];
dtostrf(altitude, 1, 2, altString);
Serial.print("Altitude: ");
Serial.println(altString);
client.publish("amrron/romeo07/altitude", altString);

// Convert the value to a char array
char co2String[8];
dtostrf(co2, 1, 2, co2String);
Serial.print("CO2: ");
Serial.println(altString);
client.publish("amrron/romeo07/co2", co2String);

// Convert the value to a char array
char tvocString[8];
dtostrf(tvoc, 1, 2, tvocString);
Serial.print("tVOC: ");
Serial.println(tvocString);
client.publish("amrron/romeo07/tvoc", tvocString);

// Convert the value to a char array
char luxString[8];
dtostrf(lux, 1, 2, luxString);
Serial.print("LUX: ");
Serial.println(luxString);
client.publish("amrron/romeo07/lux", luxString);


  Serial.print(" Temp: ");
  Serial.print((bme.readTempF()-9), 2);

  Serial.print(" Humidity: ");
  Serial.print((bme.readFloatHumidity()+10), 0);

  Serial.print(" Pressure: ");
  Serial.print(bme.readFloatPressure(), 0);

  Serial.print(" Alt: ");
  Serial.print(bme.readFloatAltitudeFeet(), 0);

  Serial.print(" CO2: ");
  Serial.print(ccs.getCO2());

  Serial.print(" tVOC: ");
  Serial.print(ccs.getTVOC());

  Serial.print(" Lux: ");
  Serial.println(apds.readLuxLevel(),2);

  delay(30000);
  client.loop();
}
