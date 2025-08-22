# 🚦 Traffic Violation Detection System

An AI-powered **Traffic Violation Detection System** built using **YOLOv8** and **Streamlit**.  
This project automatically detects and logs traffic violations such as:

- 🪖 **No Helmet Riding**
- 👨‍👩‍👦 **Triple Riding on Motorcycles**
- 📱 **Mobile Phone Use While Riding**
- 🚥 (Optional Extension) **Red-Light Jumping**

The system allows users to upload traffic videos, runs detection using a trained YOLOv8 model, and provides:
- Annotated video output
- A downloadable **violations log (CSV)**
- Interactive **dashboard on Streamlit**

---

## 📌 Problem Statement
Traffic violations in countries like India are often ignored due to limited human monitoring.  
Common violations like **riding without helmets**, **triple riding**, and **using mobile phones while riding** significantly increase road accident risks.  

This project solves the problem by providing an **automated detection pipeline** that can assist law enforcement and improve road safety.

---

## 🎯 Features
- Upload a **traffic video** and analyze it in real-time.
- Detect **helmet compliance**, **rider count per motorcycle**, and **mobile phone usage**.
- Annotated output video with bounding boxes.
- Generate and download a **CSV log of violations** with frame numbers.
- Deployed using **Streamlit** for an interactive web interface.

---

## 🛠 Tech Stack
- [YOLOv8 (Ultralytics)](https://github.com/ultralytics/ultralytics) – Object detection backbone
- [Streamlit](https://streamlit.io/) – Web UI for deployment
- [OpenCV](https://opencv.org/) – Video processing
- [Pandas](https://pandas.pydata.org/) – Violation logging

---

## 📂 Project Structure
```
Traffic_Violation_Detection/
 ├── app.py                # Main Streamlit app
 ├── best.pt               # YOLOv8 trained weights (from triple-rider-detection repo)
 ├── requirements.txt      # Dependencies
 ├── sample_videos/        # Example input videos
 ├── output.mp4            # Output (generated after detection)
 └── README.md             # Project documentation
```

---

## 📥 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Traffic_Violation_Detection.git
cd Traffic_Violation_Detection
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Download Model Weights
- Use the pretrained YOLOv8 weights from [kashishparmar02/triple-rider-detection](https://github.com/kashishparmar02/triple-rider-detection).  
- Place the file `best.pt` in the root directory.

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

---

## 🚀 Usage
1. Launch the app (`streamlit run app.py`).
2. Upload a traffic video (`.mp4`, `.avi`, `.mov`).
3. Click **Run Detection**.
4. View:
   - Annotated video with bounding boxes and labels.
   - A dataframe of violations.
   - Option to **download violations log (CSV)**.

---

## 📊 Example Output
### Input Video
Motorbike riders in Indian traffic.

### Detection Results
- `No_Helmet` → Rider detected without helmet.  
- `Triple_Riding` → More than two riders detected on one motorcycle.  
- `Mobile_Phone_Use` → Rider detected using phone while riding.  

The app highlights these violations in the video and logs them like:

| Frame | Violation          |
|-------|--------------------|
| 152   | No Helmet          |
| 280   | Triple Riding      |
| 430   | Mobile Phone Use   |

---

## 📚 Datasets
This project leverages the YOLOv8 model trained on a **custom dataset** from:
- [kashishparmar02/triple-rider-detection](https://github.com/kashishparmar02/triple-rider-detection) – 6,000+ annotated images.
- Additional datasets for validation: [RideSafe-400](https://arxiv.org/html/2503.00428v1), [TrafficCAM](https://arxiv.org/abs/2211.09620), [DriveIndia](https://arxiv.org/abs/2507.19912).

---

## 🔮 Future Improvements
- 🚥 **Red-Light Jumping Detection** using traffic signal state + vehicle movement logic.
- 📍 GPS/Time metadata integration for law enforcement use.
- 📈 Enhanced analytics dashboard with violation frequency statistics.
- ☁️ Cloud deployment on **Streamlit Cloud** or **Hugging Face Spaces**.

---

## 🤝 Contributing
Pull requests are welcome!  
Steps:
1. Fork the repo
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m 'Added new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create a Pull Request

---

## 📜 License
This project is licensed under the **MIT License** – feel free to use and modify with attribution.

---

## 🙌 Acknowledgments
- [kashishparmar02/triple-rider-detection](https://github.com/kashishparmar02/triple-rider-detection) for the pretrained model & dataset.
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for the detection framework.
- Open-source community contributions towards road safety AI projects.
