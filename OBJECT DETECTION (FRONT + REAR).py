from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

front_cam = cv2.VideoCapture(0)
rear_cam = cv2.VideoCapture(1)

def detect(frame, zone):
    results = model(frame)
    danger = False

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            name = model.names[cls]

            if name in ["person", "car", "truck", "bus"]:
                danger = True

            x1, y1, x2, y2 = box.xyxy[0]

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
            cv2.putText(frame, name, (int(x1), int(y1)-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    if danger:
        print(f"⚠️ DANGER detected in {zone}")

    return frame, danger
