#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>

const uint16_t port = 8080;
const char *host = "172.20.10.4";
WiFiClient client;

//SENSORES

//Led
int led = LED_BUILTIN;

//Sensor de Humedad - D1
int sensor = 5;

//Termistor - A0
int lectura;
int temperatura;

//Fotoresistencia D0
int luz = 16;

//Valvula - D2
int valvula = 4;


void setup(){
    
    //Led
    pinMode(led, OUTPUT);
  
    //Sensor de Humedad
    pinMode(sensor, INPUT);
    
    //Fotoresistencia
    pinMode(luz, INPUT);
    
    //Valvula
    pinMode(valvula, OUTPUT);
  
    Serial.begin(9600);
    Serial.println("Connecting...\n");
    WiFi.mode(WIFI_STA);
    WiFi.begin("PHOENIX", "Peluche343"); // change it to your ussid and password
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
}

void loop()
{
    if (!client.connect(host, port))
    {
        Serial.println("Connection to host failed");
        delay(1000);
        return;
    }
    Serial.println("Connected to server successful!");

    //Temperatura
    lectura = analogRead(A0);
    temperatura = 85.75-0.075*lectura;
    Serial.print("Temperatura: ");
    Serial.print(temperatura);
    Serial.print("° C\n\n");

    //Sensor de Humedad

    int estadoSensorHumedad;
    
    if(digitalRead(sensor) == 0){
      Serial.println("Se detecta agua\n");
      estadoSensorHumedad = 0;
    }
    else{
      Serial.println("No se detecta agua\n");
      estadoSensorHumedad = 1;
    }

    int EstadoFotoresistencia;

    //Fotoresistencia
    if(digitalRead(luz) == 0){
      Serial.println("No se detecta luz\n");
      EstadoFotoresistencia = 0;
    }
    else{
      Serial.println("Se detecta luz\n");
      EstadoFotoresistencia = 1;
    
    }

    //Valvula

    int estado_valvula;

    if(!digitalRead(sensor)){

      digitalWrite(valvula, HIGH);
      estado_valvula = 1;
    }

    else{
      digitalWrite(valvula, LOW);  
      estado_valvula = 0;
    }

    
    String myString = String("Ricardo@" + String(temperatura) + "@" + String(estadoSensorHumedad) + "@" + String(EstadoFotoresistencia) + "@" + String(estado_valvula));

    client.println(myString);
    
    //Led
    digitalWrite(led, LOW);
    delay(250);
    digitalWrite(led, HIGH);
    
    while (client.available() > 0)
    {
        char c = client.read();
        Serial.write(c);
    }
    Serial.print('\n');
    client.stop();
    delay(5000);
}
