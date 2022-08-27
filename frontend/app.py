from statistics import mode
import pandas as pd
import streamlit as st
import pickle
import xgboost

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

# def load_model_and_predict(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall):
# 	with open('/backend/deploy_xgboost.pkl', "rb") as f:
# 		loaded_model = pickle.load(f)
	
# 	prediction = model.predict(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall)
# 	return prediction



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
		gender = 0
	elif chest_pain == 'Moderate':
		gender = 3
	elif chest_pain == 'Severe':
		gender = 1
	elif chest_pain == 'Extreme':
		gender = 2
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
	if restecg == "Wave abnormality":
		restecg = 2
	if restecg == "Hypertrophy":
		restecg = 0
	features.append(restecg)
	
	# 7. restecg - resting electrocardiographic results (1 = normal; 2 = having ST-T wave abnormality; 0 = hypertrophy)

	# 8. thalach - maximum heart rate achieved

	# 9. exang - exercise induced angina (1 = yes; 0 = no)

	# 10. oldpeak - ST depression induced by exercise relative to rest

	# 11. slope - the slope of the peak exercise ST segment (2 = upsloping; 1 = flat; 0 = downsloping)

	# 12. ca - number of major vessels (0-3) colored by flourosopy

	# 13. thal - 2 = normal; 1 = fixed defect; 3 = reversable defect

	# 14. num - the predicted attribute - diagnosis of heart disease (angiographic disease status) (Value 0 = < diameter narrowing; Value 1 = > 50% diameter narrowing)



	# if True:
		
	# 	battery_power = st.number_input("How many mAh (up to 6000)", 0, 6000)

    #     if st.checkbox('Does it have bluetooth?'):
    #         blue = 'yes'
    #     else:
    #         blue = 'no'
        
    #     clock_speed = st.number_input("Clockspeed (up to 3.2 GHz)", 0.0, 3.2, .1)
        
    #     if st.checkbox('Dual SIM?'):
    #         dual_sim = 'yes'
    #     else:
    #         dual_sim = 'no'
        
    #     fc = st.number_input("Front Camera mega pixels (up to 19 MP)", 0, 19)
        
    #     if st.checkbox('Does it offer 4G?'):
    #         four_g = 'yes'
    #     else:
    #         four_g = 'no'
        
    #     int_memory = st.number_input("How much internal memory or storage (up to 512 GB)?", 2, 512)
        
    #     m_dep = st.number_input("Smartphone Depth (up to 1 cm.)", 0.1, 1.0, .1)
        
    #     mobile_wt = st.number_input("Weight of Smartphone (up to 200 g.)", 80, 200)
        
    #     n_cores = st.number_input("Number of Cores in Processor (up to 8 cores)", 1, 8)
        
    #     pc = st.number_input("Selfie Camera Mega pixels (up to 20 MP)", 0, 20)
        
    #     px_height = st.number_input("Pixel Resolution (up to 1900 pixels in Height)", 0, 1900)
        
    #     px_width = st.number_input("Pixel Resolution (up to 2600 pixels in Width)", 601, 2600)
        
    #     ram = st.number_input("How much ram (up to 6 Giga bytes)", 0, 6)
        
    #     sc_h = st.number_input("Smartphone Height (up to 190 mm)", 50, 190)
        
    #     sc_w = st.number_input("Smartphone Width (up to 180 mm)", 0, 180)
        
    #     talk_time = st.number_input("Battery Life (up to 18 hours)", 0, 18)
        
    #     if st.checkbox('Does it offer 3G?'):
    #         three_g = 'yes'
    #     else:
    #         three_g = 'no'
        
    #     if st.checkbox('Is your smartphone touch screen?'):
    #         touch_screen = 'yes'
    #     else:
    #         touch_screen = 'no'
        
    #     if st.checkbox('Does the phone offer wifi?'):
    #         wifi = 'yes'
    #     else:
    #         wifi = 'no'
        
    #     features = {'battery_power': battery_power, 'blue': blue, 'clock_speed': clock_speed, 'dual_sim': dual_sim, 'fc': fc, 'four_g': four_g, 'int_memory': int_memory, 'm_dep': m_dep, 'mobile_wt': mobile_wt, 'n_cores': n_cores, 'pc': pc, 'px_height': px_height, 'px_width': px_width, 'ram': ram, 'sc_h': sc_h, 'sc_w': sc_w, 'talk_time': talk_time, 'three_g': three_g, 'touch_screen': touch_screen, 'wifi': wifi}
        
    #     features_df = pd.DataFrame([features])    
        
    #     st.table(features_df)
        
    #     if st.button("Predict"):
    #         output = predict(loaded_model, features_df)
        
    #         st.write("The phone price is within the " + str(output) + ' category!')
      
  
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
	# model = load_model_and_predict()
	run()