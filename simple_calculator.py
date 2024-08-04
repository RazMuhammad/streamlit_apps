import streamlit as st

num1 = st.number_input("Enter your first number")
num2 = st.number_input('Enter your second number')

opreations = st.selectbox('Choose a opration',options= ("ADD" , "SUBTRACT", "MULTIPLE", "DIVIDE"))

if opreations == "ADD":
    ans = num1 + num2
elif opreations == "SUBTRACT":
    ans = num1 - num2
elif opreations == "MULTIPLE":
    ans = num1 * num2
elif opreations == "DIVIDE":
    ans = num1 / num2
else:
    ans = "Invalid Opration"

st.write(f"Result: {ans}")