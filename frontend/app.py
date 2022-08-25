import pandas as pd
import streamlit as st

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

def main():
    
    st.title("AI Service to assess risk of Heart Attack")
    st.header("Heart Attack Risk Prediction")
    st.write("This application classifies the risk of a heart attack based on age, heartrate, and types of chest pains")

    activities = ["About this AI application","Data upload and visualisation","Data preprocessing","Modeling", "Prediction"]
    st.sidebar.title("Navigation")
	# choices = st.sidebar.radio("", activities)

	# sign = False
	# train_X = pd.DataFrame()
	# test_X = pd.DataFrame()
	# train_Y = pd.DataFrame()
	# test_Y = pd.DataFrame()
	# accuracy = "Not yet defined before training"
	# f1 = "Not yet defined before training"
	# duration = "..."