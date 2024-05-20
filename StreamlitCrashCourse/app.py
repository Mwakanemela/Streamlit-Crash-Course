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
""", language="python", line_numbers=True)
#sk-proj-qMHVSf8fGKKdPxxUw1kGT3BlbkFJAqw74CBx20CZ9RGNqOIV