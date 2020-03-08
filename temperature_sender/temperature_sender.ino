#include <WiFi.h>
#include <HTTPClient.h>
 
const char* ssid = "";
const char* password =  "";

void setup() {
  Serial.begin(115200);
  delay(4000);
  WiFi.begin(ssid, password); 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
}

void loop() {
 if(WiFi.status()== WL_CONNECTED){
   HTTPClient http;
   http.begin("https://ceri.marcoaceti.it/");
   http.addHeader("Content-Type", "application/x-www-form-urlencoded");
   String request = "value=34.6";
   int code = http.POST(request);
 
   if(code > 0){
    String response = http.getString();
    Serial.println(code);
    Serial.println(response);
   }
   else{
    Serial.print("Error on sending POST: ");
    Serial.println(code);
   }
 
   http.end();
 
 }else{
 
    Serial.println("Error in WiFi connection");   
 
 }
 
  delay(10000);
 
}
