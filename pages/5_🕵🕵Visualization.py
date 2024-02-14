import streamlit as st
import pandas as pd

# ตัวอย่างข้อมูล
data = pd.DataFrame({
    "Country": ["ไทย", "อเมริกา", "จีน", "ญี่ปุ่น"],
    "Population": [70000000, 330000000, 1400000000, 125000000]
})

# แสดงชื่อกราฟ
st.title("ประชากรในบางประเทศ")

# แสดง bar chart
st.bar_chart(data, x="Country", y="Population")

st.line_chart(data, x="Country", y="Population")
st.pie_chart(data, values="Population", labels="Country")
st.scatter_plot(data, x="Country", y="Population")
