import requests

ESP32_IP = "http://192.168.1.50"

def send(cmd):
    try:
        requests.get(f"{ESP32_IP}/{cmd}")
    except:
        print("ESP32 not reachable")

def decision(front, rear):

    if front:
        print("🛑 FRONT DANGER → STOP")
        send("stop")

    elif rear:
        print("⚠️ REAR DANGER → SLOW")
        send("slow")

    else:
        print("🚗 SAFE")
        send("drive")
