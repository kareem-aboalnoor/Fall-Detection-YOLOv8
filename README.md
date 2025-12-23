# Fall Detection Using YOLOv8m

[![Project Banner]([Screenshot (113).png](https://github.com/kareem-aboalnoor/Fall-Detection-YOLOv8/blob/15203a5447df1bbe25e4046ad971afd8431a4746/Screenshot%20(113).png))](https://github.com/kareem-aboalnoor/Fall-Detection-YOLOv8/blob/15203a5447df1bbe25e4046ad971afd8431a4746/Screenshot%20(113).png)

**Real-time fall detection from video using YOLOv8m and OpenCV**

---

## 🚀 Overview

This project implements a **real-time fall detection system** using the powerful **YOLOv8m** model.  
The model was trained on a custom dataset from Roboflow and achieves high accuracy in identifying falls from video footage.

---

## 📊 Dataset

The dataset used for training was collected and annotated using **Roboflow**.

📌 **Dataset Link:**  
https://universe.roboflow.com/roboflow-universe-projects/fall-detection-ca3o8/dataset/4

---

## 🧠 Model Details

| Detail | Value |
|--------|-------|
| Architecture | YOLOv8m |
| Framework | Ultralytics YOLO |
| Training Dataset | Custom fall detection dataset (Roboflow) |
| mAP@50 | **86.9%** |
| Epochs | 50 |
| Batch Size | 8 |
| Workers | 5 |

---

## ✨ Features

✔ Real-time fall detection from video  
✔ Detects and highlights **fall events**  
✔ Person detection using YOLOv8m  
✔ Falls are marked with **red bounding boxes + confidence score**  
✔ Normal persons with **green bounding boxes**

---

## 🖼️ Example Prediction

> Replace the image below with your own example of the model predicting on a frame.

```md
![Example Prediction](path/to/your/prediction-image.png)
