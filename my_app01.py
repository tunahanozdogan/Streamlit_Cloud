import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.title("This is a title")
st.text("This is some text")
st.markdown("Streamlit is **_really_ cool** :+1:")
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.markdown("#### This is a markdown")
# Header/Subheader
st.header('This is a header')
st.subheader('This is a subheader')
# Success/Info/Error
st.success("This is a success message!")
st.info("This is a purely informational message")
st.error("This is an error!")
st.warning("This is a warning message!")
st.exception("NameError('name there is not defined')")
# Help
st.help(range)
#Write
st.write("Hello World! :sunglasses:")
st.write(range(10))
#Add image
img=Image.open("images.jpeg")
st.image(img, caption="cattie", width =300)
#Add Video
#my_video = open("ml.mov",'rb')
#st.video(my_video)
#Add youtube video
st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")
#st.balloons()

# Add checkbox
st.checkbox("Up and Down")
cbox= st.checkbox("Hide and Seek")

if cbox:
    st.write("Hide")
else:
    st.write("Seek")

# Add radio button
status = st.radio("Select a color",("blue","orange","yellow"))
st.write("My favorite color is ", status)

# Add button
st.button("Click me")

if st.button("Press me") :
    st.success("Analyze Results are..")

# Add select box
occupation=st.selectbox("Your Occupation", ["Programmer", "DataScientist", "Doctor"])
st.write("Your Occupation is ", occupation)

# Multi_select
multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])

st.write(f"You selected {len(multi_select)} number(s)")

# Slider
option1 = st.slider("Select a number", min_value=5, max_value=70, value=30, step=5)
option2 = st.slider("Select a number", min_value=0.2, max_value=30.2, value=5.2, step=0.2)

# Kullanıcıdan adını ve yaşını alıyoruz
name = st.text_input('Adınız')
age = st.number_input('Yaşınız')

# Kullanıcının hangi dilleri bildiğini seçebileceği bir çoklu seçim kutusu
languages = ['Python', 'Java', 'C++', 'JavaScript']
selected_langs = st.multiselect('Hangi programlama dillerini biliyorsunuz?', languages)

# Kullanıcının tercih ettiği renkler için bir radyo düğmesi
colors = ['Kırmızı', 'Mavi', 'Yeşil', 'Sarı']
selected_color = st.radio('Hangi rengi seversiniz?', colors)

# Formdaki tüm verileri gösteren bir düğme
if st.button('Formu Gönder'):
    st.write('Ad:', name)
    st.write('Yaş:', age)
    st.write('Bildiği Diller:', selected_langs)
    st.write('Sevdiği Renk:', selected_color)

result=option1*option2
st.write("multiplication of two options is:",result)

# Text_input
name = st.text_input("Enter your name", placeholder="Your name here")

if st.button("Submit"):
    st.write("Hello {}".format(name.title()))

# Code  # to show as if code
st.code("import pandas as pd")
st.code("import pandas as pd\nimport numpy as np")



# Echo  # it is used "with block" to draw some code on the app, then execute it
with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df

# Date input
import datetime
today=st.date_input("Today is", datetime.datetime.now())
date=st.date_input("Enter the date")



# Time input
the_time=st.time_input("The time is", datetime.time(8, 45))
hour=st.time_input(str(pd.Timestamp.now()))
st.write("Hour is", hour)

import pandas as pd
import streamlit as st
import altair as alt

df = pd.DataFrame({'x': range(1, 11), 'y': range(10, 101, 10)})

chart_type = st.radio('Hangi grafik türünü görmek istersiniz?', ['Bar', 'Histogram'])

if chart_type == 'Bar':
    chart = alt.Chart(df).mark_bar().encode(x='x', y='y')
else:
    chart = alt.Chart(df).mark_bar().encode(x=alt.X('y', bin=alt.Bin(step=10)), y='count()')

st.altair_chart(chart, use_container_width=True)

# Sidebar
st.sidebar.title("Sidebar title")
st.sidebar.header("Sidebar header")
# Sidebar with slider
a=st.sidebar.slider("input1",0,5,2,1)
x=st.sidebar.slider("input2")
st.write("# sidebar input result")
st.success(a*x)


# Dataframe
df=pd.read_csv("Advertising.csv")

# To display dataframe there are 3 methods

# Method 1
st.table(df.head())
# Method 2
st.write(df.head())  # dynamic, you can sort
st.write(df.isnull().sum())
# Method 3
st.dataframe(df.describe().T)  # dynamic, you can sort


st.markdown("#### seçenekli öngörü")
import streamlit as st
import pandas as pd

# veri setini yükleme
data = pd.read_csv("Advertising.csv")

# seçenekleri oluşturma
options = ['isnull', 'info', 'describe', 'head', 'shape']
selected_option = st.sidebar.selectbox('Ne tür bir inceleme yapmak istersiniz?', options)

# seçilen seçeneğe göre inceleme yapma
if selected_option == 'isnull':
    st.write('Null değerlerin sayısı:')
    st.write(data.isnull().sum())
elif selected_option == 'info':
    st.write('Veri setinin genel bilgileri:')
    st.write(data.info())
elif selected_option == 'describe':
    st.write('Veri setinin istatistiksel bilgileri:')
    st.write(data.describe())
elif selected_option == 'head':
    st.write('İlk 5 satır:')
    st.write(data.head())
else:
    st.write('Satır ve sütun sayısı:')
    st.write(data.shape)
    
    

# To load machine learning model
import pickle
filename = 'my_model'
model = pickle.load(open(filename, 'rb'))

# To take feature inputs
TV = st.sidebar.number_input("TV:",min_value=5, max_value=300)
radio = st.sidebar.number_input("radio:",min_value=1, max_value=50)
newspaper = st.sidebar.number_input("newspaper:",min_value=0, max_value=120)


# Create a dataframe using feature inputs
my_dict = {"TV":TV,
           "radio":radio,
           "newspaper":newspaper}

df = pd.DataFrame.from_dict([my_dict])
st.table(df)

# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success(result[0])
