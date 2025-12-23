import cv2
from ultralytics import YOLO

# Load models
fall_model = YOLO('best.pt')           
person_model = YOLO('yolov8m.pt')   

# Open video
cap = cv2.VideoCapture('fall.mp4')

# Create display window
cv2.namedWindow('Fall Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Fall Detection', 1100, 700)


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect falls
    fall_results = fall_model.predict(frame, conf=0.5)
    
    # Detect persons (class 0 in COCO = person)
    person_results = person_model.predict(frame, conf=0.5, classes=[0])
    
    # Check if fall detected
    fall_detected = len(fall_results[0].boxes) > 0
    
    if fall_detected:
        # Fall detected - Red box + label
        for box in fall_results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            
            label = f'FALL {conf:.2f}'
            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            cv2.rectangle(frame, (x1, y1 - 20), (x1 + w + 6, y1), (0, 0, 255), -1)
            cv2.putText(frame, label, (x1 + 3, y1 - 6),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    else:
        # No fall - Green box only (no label)
        for box in person_results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    cv2.imshow('Fall Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
