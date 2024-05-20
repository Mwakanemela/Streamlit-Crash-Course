import streamlit as st


# Text Element
st.text("This is a text")
st.title("This is a title:H")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("This is a super function called write")
# st.write(print("I can use write with print"))
st.markdown("""This is *markdown*""")
#integral
st.latex("\int")
st.json("""{"data": "This is streamlit json"}""")
st.code("""
print("Can also write code with streamlit")
name = Mwakanemela kayange
""", language="python", line_numbers=True)


# Error Element
st.success("This is a success")
st.error("This is error")
st.warning("Warning")
st.exception("Exception")


# Input Widget
first_name = st.text_input("Enter First Name:")
password = st.text_input("Enter Password:", type="password")
message = st.text_area("Message")
data = st.date_input("Date")
appointment_time = st.time_input("Appointment Time")
age = st.number_input("Age", min_value=0, max_value=120)
gender = st.radio("Gender", ["Male", "Female"])
enable = st.toggle("Enable Picker")
level = st.checkbox("Level")


#sk-proj-qMHVSf8fGKKdPxxUw1kGT3BlbkFJAqw74CBx20CZ9RGNqOIV