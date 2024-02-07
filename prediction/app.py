import streamlit as st
import joblib

# Load the trained model
model = joblib.load('trained_model.joblib')

# Homepage
image_path = "https://www.livemint.com/lm-img/img/2023/03/25/600x338/health-insurance-kMkD--621x414_1679762640902_1679762641259_1679762641259.jpg"
st.image(image_path,use_column_width=True)

st.title('Medical insurance cost prediction')

# Input features
age = st.slider('Enter your age', 18, 100)
sex = st.selectbox('Sex', ('Male', 'Female'))
if sex == 'Male':
    sex = 1
else:
    sex = 0

bmi = st.number_input('Enter the BMI value')
children = st.selectbox('Enter number of children', (0, 1, 2, 3, 4))
smoker = st.selectbox('Smoker', ('Yes', 'No'))
if smoker == 'Yes':
    smoker = 1
else:
    smoker = 0

region = st.selectbox('Enter your region', ('Southwest', 'Southeast', 'Northwest', 'Northeast'))
if region == 'Southwest':
    region = 1
elif region == 'Southeast':
    region = 2
elif region == 'Northwest':
    region = 3
else:
    region = 4

# Make prediction
if st.button('Predict'):
    # Corrected: Pass numerical values, not strings
    prediction = model.predict([[age, sex, bmi, children, smoker, region]])
    st.success('Your insurance cost is ${}'.format(round(prediction[0], 2)))
