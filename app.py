import streamlit as st

st.title('Streamlit Tutorial!')

st.header('GeeksForGeeks')
st.subheader('GeeksForGeeks')
st.text('GeeksForGeeks')

st.markdown('# Hi')
st.markdown('## Hi')

st.subheader('Logging:')
st.success('Success!')
st.info('Info!')
st.warning('warn!')
st.error('Error!')

st.subheader('Exception:')
st.exception(ZeroDivisionError('Div not possible')) # Exception

st.help(ZeroDivisionError)  # Help

st.write("range(1,10)")
st.write(range(1,10))
st.subheader('Arithmatic Operation:')
st.write(1*2*3)

st.subheader('Code:')
st.code('x=10 \n'
        'for i in range(x):\n'
        '\tprint(i)'
        )

st.subheader('Checkbox:')
st.checkbox('Male')
if(st.checkbox('Female')):
    st.write("You're Female!")

st.subheader('RadioButton:')
radioButton = st.radio('Select: ', ('Male','Female','Other'))

if (radioButton == 'Male'):
        st.write("You're a Male")
elif (radioButton == 'Female'):
        st.write("You're a Female")

st.subheader('Select Box:')
selectBox = st.selectbox("Data Science : ", ['Data Analysis', 'Web Scraping', 'Machine Learning', 'Deep Learning',
                                             'Natural Language Processing', 'Computer Vision', 'Image Processing'])

st.write("You've selected : ", selectBox)
st.subheader('Multiselect Box:')
multiSelectBox = st.multiselect("Data Science : ", ['Data Analysis', 'Web Scraping', 'Machine Learning', 'Deep Learning',
                                                    'Natural Language Processing', 'Computer Vision', 'Image Processing'])

st.write("You've selected : ", len(multiSelectBox), 'courses')

st.subheader('Button')
if(st.button('Click me')):
        st.write('Thanks for clicking me')

st.subheader('Slider:')
vol = st.slider('Select the Volume:', 0, 100, step=1)
st.write("Volume is:", vol)

st.subheader('Text Input:')
user = st.text_input('Username: ')
pwd = st.text_input('Password: ', type = 'password')

st.subheader('Text Area:')
st.text_area("Write something interesting")

st.subheader('Input Number:')
st.number_input('Select your age', 18, 110)

st.subheader('Input Date:')
st.date_input('Date')

st.subheader('Input Time:')
st.time_input('Time')









