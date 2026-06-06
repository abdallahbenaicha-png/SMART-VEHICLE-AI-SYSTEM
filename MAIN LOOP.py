while True:
    ret1, front = front_cam.read()
    ret2, rear = rear_cam.read()

    front_img, front_danger = detect(front, "FRONT")
    rear_img, rear_danger = detect(rear, "REAR")

    decision(front_danger, rear_danger)

    cv2.imshow("Front", front_img)
    cv2.imshow("Rear", rear_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
