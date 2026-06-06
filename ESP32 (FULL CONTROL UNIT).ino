#include <WiFi.h>
#include <WebServer.h>

#define RELAY_PIN 4

WebServer server(80);

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);

  WiFi.begin("YOUR_WIFI", "YOUR_PASS");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  Serial.println(WiFi.localIP());

  server.on("/stop", []() {
    digitalWrite(RELAY_PIN, LOW);
    Serial.println("🛑 STOP");
    server.send(200, "text/plain", "STOPPED");
  });

  server.on("/drive", []() {
    digitalWrite(RELAY_PIN, HIGH);
    Serial.println("🚗 DRIVE");
    server.send(200, "text/plain", "DRIVING");
  });

  server.on("/slow", []() {
    Serial.println("⚠️ SLOW MODE");
    server.send(200, "text/plain", "SLOW");
  });

  server.begin();
}

void loop() {
  server.handleClient();
}
