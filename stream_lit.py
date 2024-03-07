import streamlit as st
import json
import requests


st.title("Basic Calculator App for API Testing")

# Taking User Input

option = st.selectbox('What Operation do you want to Perform?',
                      ('Addition','Subtraction','Multiplication','Division'))

st.write("")
st.write("Select the Numbers from below slider ")
x=st.slider("X",0,100,20)
y=st.slider("Y",0,130,10)

#Converting the Inputs Into a Json Format
inputs ={"operation":option,"x":x,"y":y}


# When the User Clicks on the button it will fetch the API

if st.button('Calculate'):
    res = requests.post(url = "http://127.0.0.1:8000/calculate",data=json.dumps(inputs))

    st.subheader(f"Response from API = {res.text}")