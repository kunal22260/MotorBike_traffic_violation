import streamlit as st
import cv2
import tempfile
import pandas as pd
from ultralytics import YOLO


model = YOLO("best.pt")  

st.title("🚦 Traffic Violation Detection System")
st.markdown("Detects **Triple Riding**, **Helmet Compliance**, and **Mobile Phone Use**.")

# Upload video
uploaded_file = st.file_uploader("Upload Traffic Video", type=["mp4","avi","mov"])

if uploaded_file:
    # Save uploaded video to temp file
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    video_path = tfile.name
    
    st.video(video_path)

    if st.button("Run Detection"):
        cap = cv2.VideoCapture(video_path)
        width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps    = int(cap.get(cv2.CAP_PROP_FPS))

        out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        violation_log = []

        frame_id = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame_id += 1

            results = model(frame, conf=0.5)  # run inference

            for box in results[0].boxes:
                cls_id = int(box.cls[0].item())
                label = model.names[cls_id]
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Violation logging
                if label.lower() in ["triple_riding", "no_helmet", "mobile_phone_use"]:
                    violation_log.append({
                        "Frame": frame_id,
                        "Violation": label
                    })

                # Draw bounding boxes
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, label, (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

            out.write(frame)

        cap.release()
        out.release()

        st.success("✅ Detection Completed")
        st.video("output.mp4")

        # Show violation log
        if violation_log:
            df = pd.DataFrame(violation_log)
            st.dataframe(df)

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Violations Log",
                               csv,
                               "violations.csv",
                               "text/csv")
