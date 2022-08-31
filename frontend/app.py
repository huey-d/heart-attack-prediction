import pandas as pd
import streamlit as st
import pickle
import xgboost
import os
import requests
import json


# ********************************* Start HTML config ****************************************

st.set_page_config(page_title="Heart Attack Prediction", initial_sidebar_state="expanded", layout="wide", page_icon="💖")

# change the color of button widget
Color = st.get_option("theme.secondaryBackgroundColor")
s = f"""
<style>
div.stButton > button:first-child {{background-color: #fffff ; border: 2px solid {Color}; border-radius:5px 5px 5px 5px; }}
<style>
"""
st.markdown(s, unsafe_allow_html=True)

# ******************************* End HTML configuration ****************************************


def run():

	st.title("Heart Attack Risk Assessment App")

	age = st.slider("How old are you", 0, 80)

	sex = st.radio('Gender?', ("Male", "Female"))
	if sex == 'Female':
		sex = 0
	else:
		sex = 1

	cp = st.radio('Describe Chest Pain', ("None", "Moderate", "Severe", "Extreme"))
	if cp == 'None':
		cp = 0
	elif cp == 'Moderate':
		cp = 3
	elif cp == 'Severe':
		cp = 1
	elif cp == 'Extreme':
		cp = 2

	trtbps = st.slider('Resting Blood Pressure (in mm Hg)', 94, 200, 1)

	chol = st.slider('Serum cholestoral (in mg/dl)', 126, 564, 1)

	fbs = st.radio('Is fasting blood higher than 120 mg/dL', ["True", "False"])
	if fbs == 'True':
		fbs = 1
	elif fbs == 'False':
		fbs = 0

	restecg = st.radio('Resting Electrocardiographic Results', ["Normal", "Wave abnormality", "Hypertrophy"])
	if restecg == "Normal":
		restecg = 1
	elif restecg == "Wave abnormality":
		restecg = 2
	elif restecg == "Hypertrophy":
		restecg = 0
	
	thalachh = st.slider("Maximum Heart Rate", 71, 202, 1)

	exng = st.radio("Exercise induced angina", ["Yes", "No"])
	if exng == "Yes":
		exng = 1
	elif exng == "No":
		exng = 0

	oldpeak = st.slider('ST depression induced by exercise relative to rest', 0.0, 6.2, 0.1)

	slp = st.radio("Slope of peak exercise", ["Upsloping", "Flat", "Downsloping"])
	if slp == "Downsloping":
		slp = 0
	elif slp == "Flat":
		slp = 1
	elif slp == "Upsloping":
		slp = 2

	caa = st.slider("Number of major vessels", 0, 4, 1)

	thall = st.radio("thalassemia Value", ["Normal", "Fixed defect", "Reversable Defect"])
	if thall == "Fixed defect":
		thall = 1
	elif thall == "Normal":
		thall = 2
	elif thall == "Reversable Defect":
		thall = 3

	data = {'age':age,
			'sex': sex,
			'cp': cp,
			'trtbps': trtbps,
			'chol': chol,
			'fbs': fbs,
			'restecg': restecg,
			'thalachh': thalachh,
			'exng': exng,
			'oldpeak': oldpeak,
			'slp': slp,
			'caa': caa,
			'thall': thall}

	if st.button("Predict"):
		response = requests.post('http://fastapi:8000/predict', json=data)
		prediction = response.text
		st.success(prediction)

if __name__=='__main__':
	run()