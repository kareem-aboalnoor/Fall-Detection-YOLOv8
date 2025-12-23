# Fall Detection Using YOLOv8

This project implements a real-time **Fall Detection system** using **YOLOv8m**.
The model was trained on a custom dataset collected and annotated via **Roboflow**.

---

## 🚀 Project Overview
Falls represent a serious safety risk, especially for elderly individuals.
This project detects fall events in videos and highlights them in real time.

---

## 🧠 Model Details
- **Model:** YOLOv8m
- **Framework:** Ultralytics YOLO
- **Dataset:** Custom dataset from Roboflow
- **mAP@50:** **86.9%**
- **Epochs:** 50
- **Batch Size:** 8
- **Workers:** 5

---

## ✨ Features
- Real-time fall detection from video
- Green bounding boxes for normal persons
- Red bounding boxes with confidence score for fall events

---

## 🛠 Tech Stack
- Python
- YOLOv8 (Ultralytics)
- OpenCV
- PyTorch
- Roboflow

---

## 📦 Installation
```bash
pip install -r requirements.txt
