import requests
import streamlit as st
import pandas as pd
import requests



st.title("台灣氣象資料 Dashboard")

API_KEY="CWA-1B9E1D40-6BE6-42BC-9B4E-C523C3BBB1F1"
LOCATION=st.selectbox("選擇城市",["Taipei","Taichung","Kaohsiung"])#

url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={API_KEY}&format=JSON&locationName=%E8%87%BA%E5%8C%97%E5%B8%82"

response = requests.get(url, verify=False)

res = requests.get(url)
data = res.json()

location = data["records"] ["location"] [0]
st.subheader(f"{location['locationName']} 36小時預報")

for element in location ["weatherElement"]:
    name = element ["elementName"]
    value = element ["time"] [0] ["parameter"] ["parameterName"]

    st.write(f"{name} : {value}")

