import pandas as pd
import streamlit as st
import pickle
import xgboost
import os

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

def load_model_and_predict(dir_path: str = 'backend/', model_path: str = 'deploy_xgboost.pkl'):
	with open(os.path.join(dir_path, model_path), "rb") as f:
		loaded_model = pickle.load(f)
			
	return loaded_model 

def predict(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall):
	prediction = model.predict(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall)
	return prediction


def run():
	
	features = []

	st.title("Heart Attack Risk Assessment App")

	age = st.number_input("How old are you", 20, 80)
	features.append(age)

	gender = st.radio('Gender?', ("Male", "Female"))
	if gender == 'Female':
		gender = 0
	else:
		gender = 1
	features.append(gender)

	chest_pain = st.radio('Describe Chest Pain', ("None", "Moderate", "Severe", "Extreme"))
	if chest_pain == 'None':
		chest_pain = 0
	elif chest_pain == 'Moderate':
		chest_pain = 3
	elif chest_pain == 'Severe':
		chest_pain = 1
	elif chest_pain == 'Extreme':
		chest_pain = 2
	features.append(chest_pain)

	trtbps = st.slider('Resting Blood Pressure (in mm Hg)', 94, 200, 1)
	features.append(trtbps)

	chol = st.slider('Serum cholestoral (in mg/dl)', 126, 564, 1)
	features.append(chol)

	fbs = st.radio('Is fasting blood higher than 120 mg/dL', ["True", "False"])
	if fbs == 'True':
		fbs = 1
	elif fbs == 'False':
		fbs = 0
	features.append(fbs)

	restecg = st.radio('Resting Electrocardiographic Results', ["Normal", "Wave abnormality", "Hypertrophy"])
	if restecg == "Normal":
		restecg = 1
	elif restecg == "Wave abnormality":
		restecg = 2
	elif restecg == "Hypertrophy":
		restecg = 0
	features.append(restecg)
	
	thalach = st.slider("Maximum Heart Rate", 71, 202, 1)
	features.append(thalach)

	exang = st.radio("Exercise induced angina", ["Yes", "No"])
	if exang == "Yes":
		exang = 1
	elif exang == "No":
		exang = 0
	features.append(exang)

	oldpeak = st.slider('ST depression induced by exercise relative to rest', 0.0, 6.2, 0.1)
	features.append(oldpeak)

	slope = st.radio("Slope of peak exercise", ["Upsloping", "Flat", "Downsloping"])
	if slope == "Downsloping":
		slope = 0
	elif slope == "Flat":
		slope = 1
	elif slope == "Upsloping":
		slope = 2
	features.append(slope)

	ca = st.slider("Number of major vessels", 0, 4, 1)
	features.append(ca)

	thal = st.radio("Number of major vessels", ["Normal", "Fixed defect", "Reversable Defect"])
	if thal == "Normal":
		thal = 0
	elif thal == "Flat":
		thal = 1
	elif thal == "Upsloping":
		thal = 2
	features.append(thal)
	
	if st.button("Predict"):
		output = predict(features)
		
		st.write(" " + output + ' category!')
      
  
# def main():       
#     # following lines create boxes in which user can enter data required to make prediction 
    
#     Married = st.selectbox('Marital Status',("Unmarried","Married")) 
#     ApplicantIncome = st.number_input("Applicants monthly income") 
#     LoanAmount = st.number_input("Total loan amount")
#     Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
#     result =""
      
#     # when 'Predict' is clicked, make the prediction and store it 
#     if st.button("Predict"): 
#         result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 
#         st.success('Your loan is {}'.format(result))
#         print(LoanAmount)

if __name__=='__main__':
	model = load_model_and_predict()
	run()