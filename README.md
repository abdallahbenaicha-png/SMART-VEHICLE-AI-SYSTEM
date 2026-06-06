# SMART-VEHICLE-AI-SYSTEM
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/4e1b035e-00c2-4b92-a0c7-4ed39f006732" />

(RPi + ESP32 + AI Object Detection + Smart Security)
📌 Overview

This project is an AI-powered Smart Vehicle System that combines:

👁️ Real-time object detection (front & rear cameras)
🧠 Raspberry Pi AI decision engine
🔐 Vehicle security system (RFID + Fingerprint)
📍 GPS tracking system (optional module)
⚙️ ESP32 control unit (relay / car actions)
🌐 Web dashboard for monitoring & control

🖼️ System Architecture

🧠 System Workflow
Front & rear cameras capture live video
Raspberry Pi runs AI object detection (YOLO)
Decision engine analyzes risks:
obstacle detected → STOP
rear danger → SLOW
safe → DRIVE
Commands sent to ESP32 via WiFi
ESP32 controls car actions (relay / lock system)
Optional GPS tracking + dashboard visualization
⚙️ Hardware Requirements
🧠 Processing Units
Raspberry Pi 4 / 5
ESP32
📷 Sensors
Front camera (USB / CSI)
Rear camera (USB)
RFID module (RC522)
Fingerprint sensor (R305)
GPS module (optional)
⚡ Actuators
Relay module
Buzzer / alert system
💻 Software Stack
🐍 Raspberry Pi (Python)
OpenCV
YOLOv8 (Ultralytics)
Flask (Web dashboard)
Requests (ESP32 communication)
🔵 ESP32 (C++)
WiFi communication
HTTP server
GPIO relay control
RFID + fingerprint authentication
🚗 Features
👁️ AI Vision System
Object detection (car, person, truck, etc.)
Front & rear camera monitoring
Collision risk detection
🔐 Security System
RFID authentication
Fingerprint verification
Vehicle lock/unlock system
🤖 Smart Driving Logic
Automatic STOP / DRIVE decision
Rear parking safety mode
Real-time alerts
🌐 Connectivity
Raspberry Pi ↔ ESP32 communication via WiFi
Web dashboard for live status monitoring
🧱 Project Structure
Smart-Vehicle-AI-System/
│
├── raspberry_pi/
│   ├── ai_detection.py
│   ├── decision_engine.py
│   ├── gps_module.py
│   └── dashboard_flask.py
│
├── esp32/
│   ├── main.ino
│   ├── rfid_module.ino
│   └── relay_control.ino
│
├── data/
│   └── logs/
│
├── assets/
│   └── architecture.png
│
└── README.md
🚀 How It Works
▶️ 1. Run Raspberry Pi AI system
python ai_detection.py
▶️ 2. Start decision engine
python decision_engine.py
▶️ 3. Flash ESP32 firmware

Upload main.ino via Arduino IDE

▶️ 4. Connect system
Ensure Raspberry Pi and ESP32 on same WiFi network
Update ESP32 IP in Python code
🔐 ESP32 API Endpoints
Command	Action
/stop	Stop vehicle
/drive	Move forward
/slow	Caution mode
🧠 AI Model
Model: YOLOv8 nano
Classes detected:
Person 🚶
Car 🚗
Truck 🚚
Bus 🚌

👨‍💻 Author

Abdallah Ben Aicha
Embedded Systems / IoT / AI Engineering Student

⚠️ Note

This project is a prototype simulation of smart vehicle systems and not intended for real road deployment without safety validation.
