import streamlit as st
import pandas as pd

# ตัวอย่างข้อมูล
data = pd.DataFrame({
    "Country": ["ไทย", "อเมริกา", "จีน", "ญี่ปุ่น"],
    "Population": [70000000, 330000000, 1400000000, 125000000],
    "GDP": [500000000000, 25000000000000, 15000000000000, 5000000000000]
})

# แสดงชื่อกราฟ
st.title("ข้อมูลประเทศ")

# เลือกประเภทกราฟ
chart_type = st.selectbox("เลือกประเภทกราฟ", ["bar", "pie", "line", "scatter"])

# แสดงกราฟ
if chart_type == "bar":
    st.bar_chart(data, x="Country", y="Population")
elif chart_type == "pie":
    st.pie_chart(data, values="Population", labels="Country")
elif chart_type == "line":
    st.line_chart(data, x="Country", y="Population")
elif chart_type == "scatter":
    st.scatter_plot(data, x="Country", y="Population")

# แสดงข้อมูล GDP
st.write("ข้อมูล GDP")
st.table(data[["Country", "GDP"]])
