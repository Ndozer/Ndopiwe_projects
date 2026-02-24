import streamlit as web
import requests
from streamlit import *
from streamlit_lottie import *

web.set_page_config(page_title="Pixel website",layout="wide")
def soundwave(link):
    geturl = requests.get(link)
    return geturl.json()
left,right = web.columns(2)
animation = soundwave('https://assets9.lottiefiles.com/packages/lf20_l6lzuovg.json')
with left:
 web.title("Download Pixel for free")
 web.write("Pixel is a very interactive and responsive virtual assistant.")
 web.write("You can tell it many commands but if it does not know,it will not respond.")
 web.write("To give more feedback on suggestions or issues send an email to:")
 web.write("Email:"+'ndo5.create@gmail.com')
 windows = web.button("Windows")
 mac =web.button("Mac")
 if windows:
     web.write("Downloading..")
 if mac:
     web.write("Downloading..")
with left:
 web.title("Buy Pixel Preminium")
 web.write("Pixel Preminium has more features than the free version.")
 windows = web.button("Windows($2.99)")
 mac =web.button("Mac($2.99)")
 if windows:
     web.write("Are you paying through:")
     pay = web.button("PayPal")
     pay1 = web.button("Visa")
 if mac:
     web.write("Are you paying through:")
     pay = web.button("PayPal")
     pay1 = web.button("Visa")
with right:
    st_lottie(animation,height="130",key="coding")
with left:
 web.title("About Us")
 web.write("Pixel was started by a 15 year boy named Ndopiwe Zulu.He never knew how to code until he pushed himself to learn something new.")
 web.write("He watched a lot of tutorials on coding and the first language he learnt was HTML,CSS and Javascript.")
 web.write("He made a lot of websites.He never wanted to learn Python until his teacher insisted in Computer Science that his class should learn Python")
 web.write("He took up the task and learnt the basics of python.He decided to start making apps.")
 web.write("This is how Pixel was born.")
 with left:
     web.title("Commands")
     web.write("Questions:")