# 👁️Fall Detection Using YOLOv8m

![image alt](https://github.com/kareem-aboalnoor/Fall-Detection-YOLOv8/blob/1476c0483278250c7aaa8d837821b50957082dc9/Screenshot%20(113).png)

**🎥 Real-time Fall Detection from Video Using YOLOv8m and OpenCV**

This project implements a high-performance **fall detection system** capable of detecting human falls in real-time video streams. It uses the **YOLOv8m** model trained on a custom dataset from **Roboflow**, achieving excellent accuracy.  
✅ Red bounding boxes for fall events with confidence scores  
✅ Green bounding boxes for normal persons

---

## 📚 Dataset

The dataset for training was collected and annotated via **Roboflow**.  
It contains images of humans performing falls and normal activities.

📌 **Dataset Link:** [Fall Detection Dataset on Roboflow](https://universe.roboflow.com/roboflow-universe-projects/fall-detection-ca3o8/dataset/4)

---

## 🧠 Model Details

| 🔹 Detail | 🔹 Value |
|-----------|----------|
| Architecture | YOLOv8m |
| Framework | Ultralytics YOLO |
| Training Dataset | Custom fall detection dataset (Roboflow) |
| mAP@50 | 86.9% |
| Epochs | 50 |
| Batch Size | 8 |
| Workers | 5 |

---

## ✨ Features

- 🚨 Real-time fall detection from video  
- 🔴 Red bounding boxes for fall events with confidence score  
- 🟢 Green bounding boxes for normal persons  
- ⚡ Lightweight and fast inference using YOLOv8m  
- 🎯 Easy integration with video streams  

---

## 🖼️ Example Prediction

![image alt](https://github.com/kareem-aboalnoor/Fall-Detection-YOLOv8/blob/6d54e1bed4552d221d5661274a5aada3eb170a12/images/val_batch2_pred.jpg)
![image alt](https://github.com/kareem-aboalnoor/Fall-Detection-YOLOv8/blob/6d54e1bed4552d221d5661274a5aada3eb170a12/images/val_batch2_labels.jpg)

---
## 4️⃣ Installation

1. **Download or clone the repository** from GitHub.  
2. Open a terminal/command prompt in the project folder.  
3. **Create a virtual environment** (recommended):

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
