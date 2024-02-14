import json
import time 
import requests

import streamlit as st
from streamlit_lottie import st_lottie #lottieใช้สำหรับรันไฟล์
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/425c8e43-a5bb-4052-aa10-4730e06b1437/m8vsAHh86O.json"
lottie_hello = load_lottieurl(lottie_url_hello)

st.header("การพยากรณ์ข้อมูล....ด้วยเทคนิค Linear Regression")
st.header("by Kairung Hengpraprohm")

#การเรียกใช้งาาน lottie file
st_lottie(lottie_hello, key="hello")
st.balloons()