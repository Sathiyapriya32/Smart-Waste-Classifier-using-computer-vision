## 🗑️ Smart Waste Detection using Computer Vision

A real-time smart waste detection system that uses a trained model to classify waste and guide users to the correct disposal bin using computer vision. Built with **OpenCV**, **TensorFlow**, and **cvzone**.

## 📌 Features

- ♻️ Detects various types of waste using a pre-trained TensorFlow model.
- 📸 Real-time webcam input with visual feedback.
- 🧠 Intelligent bin suggestion overlay using arrow guidance.
- 🖼️ Animated waste and bin image overlays to enhance UX.

## 📁 Folder Structure

Resources/
├── background.png

├── arrow.png

├── Waste/

│ ├── 1.png to 8.png

├── Bins/

│ ├── 1.png (Recyclable)

│ ├── 2.png (Hazardous)

│ ├── 3.png (Food)

│ └── 4.png (Residual)

└── Model/

├── keras_model.h5

└── labels.txt

## 🚀 How It Works

1. Captures webcam feed.
2. Loads and runs prediction using the trained model (`keras_model.h5`).
3. Maps prediction to the correct bin using a dictionary (`classDic`).
4. Displays visual feedback for the detected waste and appropriate bin suggestion.

## 🛠️ Setup Instructions

### 🔧 Requirements

- Python 3.7 

### 📦 Installed Packages

Install the dependencies using:

```bash
pip install -r requirements.txt
```

```bash
pip install cvzone==1.5.6 opencv-python==4.5.4.60 tensorflow==2.9.1 keras==2.9.0 numpy==1.21.6
```

## 🧠 Waste Classification Labels 
| Class ID | Waste Type      | Suggested Bin |
| -------- | --------------- | ------------- |
| 1        | Cans            | Recyclable    |
| 2        | Newspaper       | Recyclable    |
| 3        | Old Shoes       | Residual      |
| 4        | Plastic Pen     | Residual      |
| 5        | Disinfectant    | Hazardous     |
| 6        | Battery         | Hazardous     |
| 7        | Vegetable Waste | Food          |
| 8        | Apple           | Food          |

## 📸 Demo Video 
Watch video :( https://drive.google.com/file/d/1KRQUXf_n8xTaDSNpsApOLpFRIj4Xd1OW/view?usp=sharing )

## 📸 Screenshots 
![Screenshot 2025-05-03 at 10 10 01 PM](https://github.com/user-attachments/assets/6ca41ba9-3608-45de-9af8-7ef22424a52b)
![Screenshot 2025-05-03 at 10 08 27 PM](https://github.com/user-attachments/assets/da407a30-fd7e-4f1a-872c-a094212cec81)
![Screenshot 2025-05-03 at 10 09 22 PM](https://github.com/user-attachments/assets/0f4437f0-7b3d-4ef5-b078-d6c9660f0e7f)
![Screenshot 2025-05-03 at 10 06 49 PM](https://github.com/user-attachments/assets/154e3390-5df0-464f-bddf-db40b0e86703)
![Screenshot 2025-05-03 at 10 06 32 PM](https://github.com/user-attachments/assets/83602df1-7f60-4111-a1d8-49062d06117d)
![Screenshot 2025-05-03 at 10 04 03 PM](https://github.com/user-attachments/assets/8ac460c7-bea9-42e2-8a76-54ac4e8a8923)
