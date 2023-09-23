import streamlit as st
import cv2

st.title("Video Oynatma Örneği")

# Video dosyasını yükleyin
video_file = st.file_uploader("car2_last.mp4", type=["mp4", "avi"])

# Video dosyası yüklendiyse oynat
if video_file is not None:
    st.video(video_file)

# Py dosyasını kaydedin ve Streamlit ile çalıştırın

