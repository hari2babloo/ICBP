import streamlit as st
st.write("Hello ,Edunet Foundation")
 
 
st.write("st.write(): This function is used to add anything to a web app")
st.title("Edunet - APP")
st.header("Content Quality Team")
st.markdown("Skill4Future")
st.subheader("TSP")
st.caption("Micro Degree")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''') 

import streamlit as st
 
st.checkbox('Yes')
st.button('Click Me')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 100)
 
 
st.number_input('Pick a number between (1-10)', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('Office time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')
st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))
st.sidebar.markdown("This is the sidebar content")
st.sidebar.title("DDRS")
st.sidebar.button("click")
st.sidebar.radio("Pick your team",["TSP","S4F","EY","CU"])
 
container = st.container()
container.write("This is written inside the container")
 
st.write("This is written outside the container") 