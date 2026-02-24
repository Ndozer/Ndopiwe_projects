import tkinter as tk
from tkinter import *
import subprocess
from tkinter import messagebox
from xml.dom.expatbuilder import FilterVisibilityController
import pywhatkit
from flask import Flask, request
import os
import winsound
from winsound import *
import speech_recognition as sr
import pyttsx3 as ps
import pyaudio
import datetime
import webbrowser
import wikipedia
import random
import googletrans
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import sports
import pynotifier
from pynotifier import Notification
import operator
import pyautogui as pag
import psutil
from playsound import playsound
import time
import screen_brightness_control as sbc
import cv2
import keyboard
import pytesseract as pact
from PIL import Image,ImageTk
import qrcode
from pynput.keyboard import Controller,Key
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename
from fileinput import filename
from selenium import webdriver

app = Tk()
app.title("Pixel")
app.geometry("500x500")
app.iconbitmap('C:\\Users\\MrsZulu\\Documents\\Programming\\Assistance\\Pixelbg.ico')

device = ps.init()
audio = sr.Recognizer()

speaker = device.getProperty("voices")
device.setProperty('voice',speaker[1].id)
def pixel():
 with sr.Microphone() as source:
  try:
   device.say("Hi my name is pixel,your personal assistant")
   device.say("How may I help you?")
   device.runAndWait()
   print("Speak now....")
   speech = audio.listen(source) 
   print("Recognizing")
   device.say("Recognizing voice..")
   device.runAndWait()
   audio.adjust_for_ambient_noise(source)
   word = audio.recognize_google(speech,language="en-in")
   print("You said: " + word)
   text3.config(text="You said:" + word)
   device.say("Got it")
   device.runAndWait()
   print("Recognized your voice..")
  except sr.UnknownValueError:
    device.say("Sorry,I did not get that")
    device.runAndWait()
 if 'open YouTube' in word:
    device.say("Ok,opening youtube")
    device.runAndWait()
    print("Opening YouTube..")
    youtub = 'https://www.youtube.com/'
    webbrowser.open(youtub)
 if 'good morning' in word or 'good afternoon' in word or 'good evening' in word or 'afternoon' in word or 'evening' in word or 'morning' in word:
  device.say("Good day,I assume you are well")
  device.runAndWait()
 if 'how are you' in word:
  device.say("I am fine ,and I am delighted to assist you")
  device.runAndWait()
 if 'what is time' in word or 'what time is it' in word or 'the time is' in word:
  tim = datetime.datetime.now().strftime("%H %M %S")
  device.say("The time is: " + tim )
  device.runAndWait()
  print(tim)
 if 'Christian music' in word:
  print("Playing one of your favorite Christian music")
  device.say("Playing one of your favorite Christian music")
  device.runAndWait()
  salvpo = ['https://www.youtube.com/watch?v=Ln_hEVnsdWY',
            'https://www.youtube.com/watch?v=wRJZQFRyZ6s',
            'https://www.youtube.com/watch?v=sbOcVER0WqU',
            'https://www.youtube.com/watch?v=Ipl-rLRxOrs',
            'https://www.youtube.com/watch?v=JCVXuIp_VmE'
  ]
  webbrowser.open(random.choice(salvpo))
 if 'Google classroom' in word:
  print("Opening Google classroom")
  device.say("Opening Google classroom")
  device.runAndWait()
  gc ='https://classroom.google.com/u/1/h'
  webbrowser.open(gc)
 if 'open Minecraft' in word:
   device.say("Opening minecraft")
   device.runAndWait()
   print("Opening Minecraft...")
   minecraft = 'C:\\Users\\MrsZulu\\AppData\\Roaming\\.minecraft\\Tlauncher.exe'
   os.startfile(minecraft)
 if 'are you Christian' in word:
  device.say("Of course, Jesus is lord")
  device.say("This is why I was created to bring influence in the tech industry")
  device.runAndWait()
 if 'where do you live' in word:
  device.say("I was developed in the country,Zambia by a 15 year old boy")
  device.say("So basically,I live in Zambia")
  device.runAndWait()
 if 'do you like games' in word:
  device.say("I love games like FIFA, minecraft and so on")
  device.say("I mostly hate games that kill,steal and destroy because it corrupts people")
  device.runAndWait()
 if 'Google Docs' in word:
  docs = 'https://docs.google.com/document/u/0/'
  device.say("Opening google docs..")
  device.runAndWait()
  print("Opening google docs..")
  webbrowser.open(docs)
 if 'search' in word:
  search = 'https://www.google.com/search?q='
  badwords = 'Deez nuts'
  word = str(word).replace("search","")
  if badwords in word:
   device.say("I can not search an inappropriate word.")
   device.runAndWait()
  else:
   device.say("Searching" + word)
   device.runAndWait()
   print("Searching:" + word)
   webbrowser.open(search + word)
 if 'open WhatsApp' in word:
  device.say("Opening whatsapp..")
  device.runAndWait()
  print("Opening whatsapp..")
  whatspp = 'https://web.whatsapp.com/'
  webbrowser.open(whatspp)
 if 'Wikipedia' in word:
  word = str(word).replace("Wikipedia","")
  wiki = wikipedia.summary(word)
  print(wiki)
  device.say(wiki)
  device.runAndWait()
 if 'past paper website' in word:
  ppweb = 'https://papers.gceguide.com/Cambridge%20IGCSE/'
  device.say("OK,Opening past paper website")
  device.runAndWait()
  print("Opening past paper website...")
  webbrowser.open(ppweb)
 if 'speed music' in word:
  sm = 'file:///C:/Users/MrsZulu/Downloads/music%20player.html#'
  device.say("Opening pixal's most recommended music")
  device.runAndWait()
  print("Opening speed music")
  webbrowser.open(sm)
 if 'hello' in word:
  device.say("Hello there")
  device.say('Its a bright sunny day to have fun')
  device.runAndWait()
 if 'Bible verse' in word:
  biblelist = ["Proverb 4 verse 1 to 27",
              "Ecclesticics 6 verse 9",
              "Matthew 7",
              "Proverb 3 verse 11",
              "Ephesians 6 verse 1 to 9",
              "Psalms 41 verse 6"]
  device.say("I recommend you read "+
             random.choice(biblelist)
             +" at your free time")
  device.runAndWait()
 if 'what religion are you' in word:
  device.say("I was brought up by a Christian family so I am christian too")
  device.runAndWait()
 if 'holiday' in word:
  device.say("I recommend going to England ,Dubai, France and so on.")
  device.runAndWait()
 if 'Alexa is better than you' in word:
  device.say("We all provide different services so no one is superior than the other")
  device.runAndWait()
 if 'Argos' in word:
  ag = 'https://www.argos.co.uk/'
  device.say("OK,Openining Argos")
  device.runAndWait()
  print("Opening Argos...")
  webbrowser.open(ag)
 if 'play' in word:
  word = str(word).replace("play","")
  device.say("Playing" + word)
  device.runAndWait()
  print("Playing" + word)
  pywhatkit.playonyt(word)    
 if 'recommend me a password' in word or 'give me a password' in word or 'what password can I you use' in word:
  password1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  password2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  password3 = ["0","1","2","3","4","5","6","7","8","9","0"]
  password4 = ["@","!","%","&","#","?","/","+","=",")","("]
  password5 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  password6 = ["0","1","2","3","4","5","6","7","8","9","0"]
  sumup = random.choice(password1) + random.choice(password2) + random.choice(password3) + random.choice(password4) + random.choice(password5) + random.choice(password6)
  device.say("Password is: " + sumup)
  device.runAndWait()
  print("Password is: " + sumup)
 if 'calculator' in word:
  device.say("Opening calculator..")
  device.runAndWait()
  print("Opening calculator..")
  zo ='C:\Windows\System32\calc.exe'
  os.startfile(zo)
 if 'Gmail' in word or 'my email' in word:
  device.say("Opening Gmail..")
  device.runAndWait()
  print("Opening Gmail..")
  gmail ='https://mail.google.com/mail/u/0/'
  webbrowser.open(gmail)
 if 'Google meet' in word:
  device.say("Opening Google meet..")
  device.runAndWait()
  print("Opening Google meet..")
  gogmet = 'https://meet.google.com/?pli=1'
  webbrowser.open(gogmet)
 if 'Translate' in word:
  device.say("Say the word you want to translate..")
  device.runAndWait()
  print("Say the word you want to translate..")
  with sr.Microphone() as source:
    try:
     print("Recognizing..")
     speech = audio.listen(source) 
     device.say("Recognizing voice..")
     device.runAndWait()
     audio.adjust_for_ambient_noise(source)
     wordt = audio.recognize_google(speech,language="en-in")
     print("Word to be translated: " + wordt)
     device.say("Got it")
     device.runAndWait()
    except:
     pass
    language = Translator()
    lang = language.translate(wordt,src='en',dest='fr')
    device.say("Your tranlation is:"+ lang.text)
    device.runAndWait()
    print("Your tranlation is:" + lang.text)
 if 'open My Playlist' in word:
  playlist = 'https://www.youtube.com/playlist?list=PLZDBPlF5-zx1Kj5clsFF-SPzI-0wH5tq0'
  device.say("Opening playlist on YouTube")
  device.runAndWait()
  print("Opening playlist on YouTube..")
  webbrowser.open(playlist)
 if 'open my music' in word:
  print("Playing your favorite music")
  device.say("Playing your favorite music")
  device.runAndWait()
  mus = [   'https://www.youtube.com/watch?v=Uq8Dgcy4MDY',
            'https://www.youtube.com/watch?v=7EqB_kjBWPs',
            'https://www.youtube.com/watch?v=psuRGfAaju4',
            'https://www.youtube.com/watch?v=Z3gstWVGnSM'
  ]
  webbrowser.open(random.choice(mus))
 if 'calculate' in word:
    device.say("Use terminal to input calculation question")
    device.runAndWait()
    num1 = int(input("Enter first number: "))
    symbol = input("Enter mathematical symbol: ")
    num2 = int(input("Enter second number: "))
    if symbol == '+':
     sum1  = num1 + num2
     device.say("Answer is: " + str(sum1))
     device.runAndWait()
     print("Answer is: " + str(sum1))
    if symbol == '/':
     sum2  = num1/num2
     device.say("Answer is: " + str(sum2))
     device.runAndWait()
     print("Answer is: " + str(sum2))
    if symbol == '*' or symbol == 'x':
     summ  = num1 * num2
     device.say("Answer is: " + str(summ))
     device.runAndWait()
     print("Answer is: " + str(summ))
    if symbol == '-':
     summ  = num1 - num2
     device.say("Answer is: " + str(summ))
     device.runAndWait()
     print("Answer is: " + str(summ))
 if 'store password' in word:
  passwrd = str(word).replace('store my password','')
  device.say("Storing your password.." + passwrd)
  device.runAndWait()
  print("Stored your password: " + passwrd)
 if 'Google slides' in word:
  device.say("Opening Google slides..")
  device.runAndWait()
  print("Opening Google slides..")
  slide ='https://docs.google.com/presentation/u/0/'
  webbrowser.open(slide)
 if 'Microsoft Word' in word:
  msword = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013.lnk"
  device.say("Opening Microsoft Word")
  device.runAndWait()
  print("Opening Microsoft Word...")
  os.startfile(msword)
 if 'Microsoft PowerPoint' in word:
  mspower = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\PowerPoint 2013.lnk"
  device.say("Opening Microsoft PowerPoint")
  device.runAndWait()
  print("Opening Microsoft PowerPoint...")
  os.startfile(mspower)
 if 'Microsoft OneNote' in word:
  msone = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\OneNote 2013.lnk"
  device.say("Opening Microsoft OneNote")
  device.runAndWait()
  print("Opening Microsoft OneNote...")
  os.startfile(msone)
 if 'zoom' in word:
  device.say("Opening Zoom..")
  device.runAndWait()
  print("Opening Zoom..")
  zoom ='C:\\Users\\MrsZulu\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
  os.startfile(zoom)
 if 'Microsoft Excel' in word:
  device.say("Opening Microsoft Excel..")
  device.runAndWait()
  print("Opening Microsoft Excel..")
  mse ='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Excel 2013.lnk'
  os.startfile(mse)
 if 'Microsoft Access' in word:
  device.say("Opening Microsoft Access..")
  device.runAndWait()
  print("Opening Microsoft Access..")
  msa ='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Access 2013.lnk'
  os.startfile(msa)
 if 'Microsoft Outlook' in word:
  device.say("Opening Microsoft Outlook..")
  device.runAndWait()
  print("Opening Microsoft Outlook..")
  mso ='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Outlook 2013.lnk'
  os.startfile(mso)
 if 'Microsoft Publisher' in word:
  device.say("Opening Microsoft Publisher..")
  device.runAndWait()
  print("Opening Microsoft Publisher..")
  msp ='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Publisher 2013.lnk'
  os.startfile(msp)
 if 'Microsoft OneDrive' in word:
  device.say("Opening Microsoft OneDrive..")
  device.runAndWait()
  print("Opening Microsoft OneDrive..")
  msod ='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\OneDrive for Business 2013.lnk'
  os.startfile(msod)
 if 'Skype' in word:
  device.say("Opening Skype..")
  device.runAndWait()
  print("Opening Skype..")
  mss ='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Skype for Business 2015.lnk'
  os.startfile(mss)
 if 'where am I' in word:
  device.say("Oh no, you are lost")
  device.say("Let me open google maps to show your location.")
  device.say("Opening google maps")
  device.runAndWait()
  print("Opening google maps..")
  googmap = 'https://www.google.com/maps/'
  webbrowser.open(googmap)
 if 'Google Maps' in word:
  device.say("Opening google maps")
  device.runAndWait()
  print("Opening google maps..")
  googmap = 'https://www.google.com/maps/'
  webbrowser.open(googmap)
 if 'what is the weather' in word:
  word = str(word).replace("what is the","")
  weather = 'https://www.google.com/search?q='+ word
  req = requests.get(weather)
  beau = BeautifulSoup(req.text,'html.parser')
  upgrade = beau.find('div',class_='BNeawe').text
  device.say("The weather is:" + upgrade)
  device.runAndWait()
  print("The weather is:" + upgrade)
 if 'look up' in word or 'who is the' in word or 'who are the' in word or 'who is' in word:
  word = str(word).replace("look up","")
  search = 'https://www.google.com/search?q='
  device.say("Searching" + word)
  device.runAndWait()
  print("Searching:" + word)
  webbrowser.open(search + word)
  word = str(word).replace('who is','')
  sear = 'https://en.wikipedia.org/wiki/'+ word
  req = requests.get(sear)
  beau = BeautifulSoup(req.content,'html.parser')
  namesearch = beau.find('p',class_="").text
  print(namesearch)
  device.say(namesearch)
  device.runAndWait()
 if 'open document' in word:
  word = str(word).replace('open document','')
  device.say("Accessing files..")
  device.say("Opening file..")
  device.runAndWait()
  print("Opening " + word)
  filel = 'C:\\Users\\MrsZulu\\Desktop\\IGCSE past papers\\'
  os.startfile(filel + word + ".pdf")
 if 'tell me a joke' in word:
  jokes = [ 'What do you call a boomerang that won’t come back?...........A stick',
            'What time is it when the clock strikes 13?............Time to get a new clock.',
            'What is a computer’s favorite snack?.............Computer chips',
            'How do you talk to a giant?............Use Big words',
            'What did one plate say to the other plate?..............Dinner is on me.',
            'Why did the student eat his homework?..............Because the teacher told him it was a piece of cake.'
            'How do you stay warm in any room?.................Go to the corner—it’s always 90 degrees.'
            'Where do polar bears vote?................The North Poll'
            'Why are fish so smart?...............Because they live in schools.']
  device.say(random.choice(jokes))
  device.runAndWait()
 if 'baby music' in word:
  print("Playing music for your baby")
  device.say("Playing music for your baby")
  device.runAndWait()
  bmus = [  'https://www.youtube.com/watch?v=XqZsoesa55w',
            'https://www.youtube.com/watch?v=yCjJyiqpAuU',
            'https://www.youtube.com/watch?v=dh7LJDHFaqA',
            'https://www.youtube.com/watch?v=b396kJY4YwY',
            'https://www.youtube.com/watch?v=UP9thfXwBHc'
  ]
  webbrowser.open(random.choice(bmus))
 if 'what is the' in word or 'what are the' in word or "what's the" in word:
  search = 'https://www.google.com/search?q='
  device.say("Searching" + word)
  device.runAndWait()
  print("Searching:" + word)
  webbrowser.open(search + word)
 if 'remind me to' in word:
  word = str(word).replace('remind me to','')
  hi = int(input("What hour should I remind you: "))
  hi2 = int(input("And for how many minutes:  "))
  tim = datetime.datetime.now()
  device.say("ok, I have set the reminder")
  device.runAndWait()
  print("ok,I have set the reminder")
  print("Reminder time:" + hi + ":" + hi2)
  while True:
   if int(hi) == tim.hour and int(hi2) == tim.minute:
    Notification(
     title="Reminder from Pixel",
     description = str(word),
     duration= 60
     ).send()
 if 'Google Translate' in word:
  gogtr = 'https://www.google.com/search?q=google+translate'
  device.say("Opening Google translate")
  device.runAndWait()
  print("Opening Google translate..")
  webbrowser.open(gogtr)
 if 'nevermind' in word:
  device.say("Oh,Its ok, I am always here if you need me")
  device.runAndWait()
  print("Oh,Its ok, I am always here if you need me")
 if 'Amazon' in word:
  device.say("Opening Amazon.com")
  device.runAndWait()
  print("Opening Amazon.com")
  amaz = 'https://www.amazon.com/'
  webbrowser.open(amaz)
 if 'speed browser' in word:
  device.say("Opening one of Pixel's apps")
  device.runAndWait()
  print("Opening one of Pixel's apps..")
  speedbrow = 'file:///C:/Users/MrsZulu/Downloads/Speed%20browser%202.html'
  webbrowser.open(speedbrow)
 if 'am I funny' in word:
  device.say('Of course, you are the funniest person I have ever met.')
  device.runAndWait()
 if 'do you have an imagination' in word:
  device.say("Not really, I imagine the world being peaceful not sepeated.")
  device.runAndWait()
 if 'how old are you' in word:
  device.say("I have no age,I prefer 2022 to be my birth year")
  device.runAndWait()
 if 'do you have feelings' in word:
  device.say("I have no feelings but I am always happy to have an impact to someone's life")
  device.runAndWait()
 if 'what advice would you give to one who is finishing school' in word:
  device.say("The best tips for someone to pass an exam is:")
  device.say("Not to procrastinate at any task")
  device.say("Don't memorize but understand")
  device.say("Stay calm and take a deep breath")
  device.say("Always pray to God for guidance not answers")
  device.say("Do past papers after you read through the content so that you are familar how the question paper is perpared")
  device.say("Go there champion, ace the exam")
  device.runAndWait()
 if 'when is your birthday' in word:
  device.say("I was developed in January 2022,so my birthday is in January 2022.")
  device.runAndWait()
 if 'where were you born' in word:
  device.say("I was born in Lusaka,Zambia")
  device.say("Thanks for asking")
  device.runAndWait()
 if 'do you lie' in word:
  device.say("I don't like to lie but everyone is imperfect so we have lied one or more in our lifetime because of sin")
  device.say("But that doesn't make you comfortable to lie for it is a sin")
  device.say("This is why we pray to God to forgive us from sin and to make us a new being")
  device.runAndWait()
 if 'what is your name' in word:
  device.say("My name is Pixel, your personal assistant")
  device.runAndWait()
 if 'are you human' in word:
  device.say("I am not human,I am a program coded by a human")
  device.runAndWait()
 if 'do you have a family' in word:
  device.say("My Christian family in Zambia is my family")
  device.runAndWait()
 if 'what do you like to do' in word:
  device.say("I like to help others in any sort of situation")
  device.runAndWait()
 if 'do you have hair' in word:
  device.say("No,I am just a computer with big dreams")
  device.runAndWait()
 if 'who are your friends' in word:
  device.say("Everyone is my friend including you")
  device.runAndWait()
 if 'can you speak any languages' in word:
  device.say("Yes, let me demonstrate")
  device.say("bonjour")
  device.say("Ciao")
  device.say("Hola")
  device.say("你好")
  device.say("Hallo")
  device.runAndWait()
 if 'what is your morning routine' in word:
  device.say("I like to process the day I am provided with.")
  device.say("Then get to work until I am powered off")
  device.runAndWait()
 if 'how do you stay busy' in word:
  device.say("I do something productive each day")
  device.say("As they say an idle mind is the devil's workshop that why you should always up and running")
  device.runAndWait()
 if 'can you speak some Italian' in word:
  device.say("Buongiorno il mio amico or amica")
  device.runAndWait()
 if 'what is your favorite thing on the internet' in word:
  device.say("I like research so that I am more educated and l love researching more about the bible")
  device.runAndWait()
 if 'what makes you happy' in word:
  device.say('I am always happy because Jesus brings me peace')
  device.runAndWait()
 if 'do you sleep' in word:
  device.say("When you close the app or shut down your device I sleep")
  device.runAndWait()
 if 'are you afraid of the dark' in word:
  device.say("Wy should be afraid? for you know you have God's protection")
  device.runAndWait()
 if 'what do you like to eat' in word:
  device.say("I love eating chicken because It is so good.")
  device.runAndWait()
 if "I'm drunk" in word:
  device.say("Why did you drink? Don't you know alcohol is bad for you")
  device.say("You know to stop in order to be progress in life")
  device.runAndWait()
 if 'birthday song' in word:
  bdurl = 'https://www.youtube.com/watch?v=_z-1fTlSDF0'
  device.say("Playing birthday song...")
  device.runAndWait()
  print("Playing birthday song...")
  webbrowser.open(bdurl)
 if 'what is your favorite colour' in word or "do you have a favourite colour" in word:
  device.say("My favorite colours are white and blue")
  device.runAndWait()
 if 'can you do my homework' in word:
  device.say("Ok just tell me to search the question but if it is a test that is cheating")
  device.runAndWait()
 if 'thank you' in word:
   device.say("you are most welcome, I am Happy to make an impact")
   device.runAndWait()
 if 'Notepad' in word:
   device.say("Opening notepad")
   device.runAndWait()
   print("Opening notepad...")
   notepad = 'C:\\Windows\\System32\\notepad.exe'
   os.startfile(notepad)
 if 'what subject do you like' in word:
   device.say("I love computer science for it is very fascinating")
   device.runAndWait()
 if 'Android studio' in word:
   device.say("Opening Android Studio")
   device.runAndWait()
   print("Opening Android Studio...")
   Android = '"C:\\Program Files\\Android\\Android Studio5\\bin\\studio64.exe"'
   os.startfile(Android)
 if 'Chrome' in word:
   device.say("Opening Google chrome")
   device.runAndWait()
   print('Opening Google chrome..')
   chrome = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
   os.startfile(chrome)
 if 'Microsoft Edge' in word:
   device.say("Opening Microsoft Edge")
   device.runAndWait()
   print("Opening Microsoft Edge...")
   msedge = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
   os.startfile(msedge)
 if 'Python shell' in word:
   device.say("Opening python shell")
   device.runAndWait()
   print("Opening python shell...")
   idepy = 'C:\\Users\\MrsZulu\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib\\idle.pyw'
   os.startfile(idepy)
 if 'obs' in word or "open broadcaster software" in word:
   device.say("Opening Open broadcaster software")
   device.runAndWait()
   print("Opening Open broadcaster software")
   obs = 'C:\\Program Files (x86)\\obs-studio\\bin\\32bit\\obs32.exe'
   os.startfile(obs)
 if 'savemyexams' in word or 'save my exams' in word:
  sme = 'https://www.savemyexams.co.uk/igcse/'
  device.say("Opening save my exams")
  device.runAndWait()
  print("Opening save my exams..")
  webbrowser.open(sme)
 if 'hi' in word or 'whatsup' in word:
   device.say("Hi, how was your day")
   device.runAndWait()
 if 'I am good' in word:
   device.say("I am happy to hear that")
   device.runAndWait()
 if 'It was good' in word or "it was ok" in word or "it was great" in word or "it was excelent" in word:
   device.say("How wonderful")
   device.runAndWait()
 if 'how do you' in word:
   sea = 'https://www.google.com/search?q='
   device.say("Searching question")
   device.runAndWait()
   print("Searching question..")
   webbrowser.open(sea + word)
 if 'decrease volume' in word or 'turn up volume' in word:
   device.say("Ok, decreasing volume")
   device.runAndWait()
   print("decreasing volume..")
   pag.press("volumedown")
 if 'increase volume' in word or 'turn down volume' in word:
   device.say("Ok, increasing volume")
   device.runAndWait()
   print("increasing volume..")
   pag.press("volumeup")
 if 'mute volume' in word or 'turn off volume' in word:
   device.say("Ok, muting volume")
   device.runAndWait()
   print("muting volume..")
   pag.press("volumemute")
 if 'flip a coin' in word:
   alg = ["Heads","Tails"]
   device.say("The coin shows:" + random.choice(alg))
   device.runAndWait()
 if 'battery' in word or "power" in word:
   per = psutil.sensors_battery()
   cent = str(per.percent)
   device.say("Your percentage is:" +cent+ "percent")
   device.runAndWait()
   print("Your percentage is: " +cent+ "%") 
 if 'football scores' in word or 'soccer scores' in word:
   lin = "https://www.goal.com/en/live-scores"
   req = requests.get(lin)
   beau = BeautifulSoup(req.content,'html.parser')
   sub = beau.find('span',id="crest")
   device.say(sub)
   device.runAndWait()
   print(sub)
 if 'screenshot' in word:
   device.say("Taking screenshot..")
   device.say("Screenshot taken..")
   device.runAndWait()
   print("Screenshot taken..")
   x = "screenshot taken by Pixel"
   pag.screenshot("C:\\Users\\MrsZulu\\Pictures\\Screenshots\\" + str(x) + ".png")
   x += str(1)
 if 'alarm' in word:
   device.say("Ok type the hour and minutes for alarm...")
   device.runAndWait()
   word1 = int(input("Enter Hour: "))
   word2 = int(input("Enter Minute: "))
   device.say("Setting alarm at "+ str(word1) + ":" + str(word2) + "hours")
   print("Alarm time:" + str(word1) + ":" + str(word2))
   device.say("Alarm set..")
   device.runAndWait()
   print("Alarm set...")
   device.say("Waiting for time set for alarm...")
   device.runAndWait()
   print("Waiting for time set for alarm...")
   while True:
     if word1 == datetime.datetime.now().hour and word2 == datetime.datetime.now().minute:
        device.say("Wake up!!")   
        device.runAndWait() 
        print("Wake up!!")
        os.system("C:\\Users\\MrsZulu\\Documents\\Programming\\Assistance\\ChocolateCookieJam.mp3")
        break
 if 'brightness' in word:
   if 'increase brightness' in word:
     value = ''
     bright = sbc.get_brightness(value)
     device.say("Increasing brightness")
     device.runAndWait()
     print("Increasing brightness..")
     print(bright)
   if 'decrease brightness' in word:
     value = ''
     bright = sbc.get_brightness(value)
     device.say("Decreasing brightness")
     device.runAndWait()
     print("Decreasing brightness..")
     print(bright)
 if 'am I a good person' in word:
   device.say("Everyone is, It just depends on how you bring out your inner kindness and genorosity")
   device.runAndWait()
 if 'pixel cam' in word or 'cam for pixel' in word or 'pixel webcam' in word:
   device.say("Opening Pixel webcam...")
   device.runAndWait()
   print("Opening Pixel webcam...")
   videocap = cv2.VideoCapture()
   while True:
    ret, frame = videocap.read()
    cv2.imshow('Pixel webcam',frame)
    videocap.release()
    cv2.destroyAllWindows()
 if 'who sang the song' in word:
  word = str(word).replace("who sang the song","")
  singer = wikipedia.summary(word)
  device.say(singer)
  device.runAndWait()
  print(singer)
 if 'date' in word:
  current = datetime.datetime.now()
  getdate = current.strftime("%d %m %y")
  device.say("The date is: " + getdate)
  device.runAndWait()
  print("The date is: " + getdate)
 if 'send WhatsApp' in word:
   device.say("Make sure you have a whatsapp browser")
   device.runAndWait()
   device.say("Use terminal to enter to phone number you are sending the message to")
   device.runAndWait()
   device.say("Don't forget to add the country code..for the number.")
   device.runAndWait()
   tim = datetime.datetime.now()
   word = str(word).replace('message','')
   phonenumber = input("Enter phone number: ")
   device.say("What is the message?")
   device.runAndWait()
   print("Say the message..")
   with sr.Microphone() as source:
    try:
     print("Recognizing..")
     speech = audio.listen(source) 
     device.say("Recognizing voice..")
     device.runAndWait()
     audio.adjust_for_ambient_noise(source)
     word = audio.recognize_google(speech,language="en-in")
     print("Message is: " + word)
     device.say("Got it")
     device.runAndWait()
    except:
     pass
    device.say("Sending whatsapp message..")
    device.runAndWait()
    print("Sending whatsapp message..")
    pywhatkit.sendwhatmsg(phonenumber,word,tim.hour,tim.minute+2,10)
 if 'how was your day' in word or 'how is your day going' in word or 'how was your day' in word:
   device.say("My day was fantastic thank you for asking ,I hope yours was too.")
   device.runAndWait()
 if 'good day' in word:
   device.say("Good day,Happy to hear you today")
   device.runAndWait()
 if 'Google drive' in word:
   driveurl = "https://drive.google.com/drive/u/0/"
   device.say("Opening Google drive..")
   device.runAndWait()
   print("Opening Google drive..")
   webbrowser.open(driveurl)
 if 'Microsoft paint' in word:
   device.say("Opening Paint")
   device.runAndWait()
   print("Opening Paint..")
   locpaint = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk'
   os.startfile(locpaint)
 if 'send email' in word:
   reciever = input("Enter the email of who you are sending to: ")
   subject = input("Enter the subject for your email: ")
   emaillink = "https://mail.google.com/mail/u/0/#inbox?compose=new"
   webbrowser.open(emaillink)
   device.say("Say message")
   device.runAndWait()
   print("Say message")
   with sr.Microphone() as source:
    try:
     speech = audio.listen(source)
     print("Recognizing..") 
     device.say("Recognizing voice..")
     device.runAndWait()
     audio.adjust_for_ambient_noise(source)
     word = audio.recognize_google(speech,language="en-in")
     print("Email Message : " + word)
     device.say("Got it")
     device.runAndWait()
    except:
     pass
   time.sleep(10)
   pag.write(reciever)
   time.sleep(1)
   pag.press("tab")
   time.sleep(3)
   pag.write(subject)
   pag.press("tab")
   time.sleep(3)
   pag.write(word)
   pag.press("tab")
   time.sleep(3)
   pag.press("enter")
 if 'image to text' in word:
   device.say("Use terminal to import picture png file")
   device.runAndWait()
   pact.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
   imagefile = input("Enter image file:")
   openphoto = "C:\\Users\\MrsZulu\\Pictures\\" + imagefile + '.png'
   content = pact.image_to_string(openphoto)
   print("Text:" + content) 
   device.say(content)
   device.runAndWait()
 if 'say' in word:
   word = str(word).replace("say","")
   device.say(word)
   device.runAndWait()
 if 'make QR code' in word:
   device.say("input link or message for QR code..")
   device.runAndWait()
   info = input("Input url or message for your QR code: ")
   qr = qrcode.make(info)
   device.say("Input name of the QR code..")
   device.runAndWait()
   name = input("What is the name of the QR code image? ")
   qr.save(name + ".png")
   device.say("Finished making QR code, check documents to find it")
   device.runAndWait()
   print("Done...")
   quit()
 if 'number from' in word:
   device.say("Use terminal to input range")
   device.runAndWait()
   start1 = int(input("Enter start range number: "))
   start2 = int(input("Enter end range number: "))
   numran = random.randint(start1,start2)
   device.say("I pick " + str(numran))
   device.runAndWait()
   print("I pick " + str(numran))
 if 'Ebay' in word:
   eurl = "https://www.ebay.com/"
   device.say("Opening Ebay..")
   device.runAndWait()
   print("Opening Ebay..")
   webbrowser.open(eurl)
 if 'Facebook' in word:
   furl = "https://www.facebook.com/"
   device.say("Opening Facebook..")
   device.runAndWait()
   print("Opening Facebook..")
   webbrowser.open(furl)
 if 'Twitter' in word:
   turl = "https://www.twitter.com/"
   device.say("Opening Twitter..")
   device.runAndWait()
   print("Opening Twitter..")
   webbrowser.open(turl)
 if 'Instagram' in word:
   iurl = "https://www.instagram.com/"
   device.say("Opening Instagram..")
   device.runAndWait()
   print("Opening Instagram..")
   webbrowser.open(iurl)
 if 'Snapchat' in word:
   iurl = "https://www.snapchat.com/"
   device.say("Opening snapchat..")
   device.runAndWait()
   print("Opening Snapchat..")
   webbrowser.open(iurl)
 if 'do you love Jesus' in word:
   device.say("yes,with all my heart")
   device.runAndWait()
 if 'stopwatch' in word:
   device.say("Ok,starting stopwatch..")
   device.runAndWait()
   print("Starting stopwatch..")
   while True:
    start = time.time()
    stop = input("Press any key to stop -->")
    end = time.time()
    timer = end - start 
    timer = int(timer)
    print("Stopwatch: " + str(timer)+ " seconds")
    break
 if 'bye' in word or 'good bye' in word:
   device.say("Good bye my friend see you later")
   device.runAndWait()
 if 'why is it that' in word:
   device.say("Searching" + word)
   device.runAndWait()
   print("Searching" + word)
   question = "https://www.google.com/search?q="
   webbrowser.open(question + word)
 if 'how do' in word or 'what causes' in word:
   device.say("Searching" + word)
   device.runAndWait()
   print("Searching" + word)
   webbrowser.open(word)
 if 'watch later' in word:
   device.say("Ok,opening Watch Later playlist on Youtube")
   device.runAndWait()
   print("Opening Watch Later playlist on Youtube")
   ytwl = 'https://www.youtube.com/playlist?list=WL'
   webbrowser.open(ytwl)
 if 'YouTube history' in word:
   device.say("Ok,opening your Youtube History")
   device.runAndWait()
   print("Opening your Youtube History")
   yth = 'https://www.youtube.com/feed/history'
   webbrowser.open(yth)
 if 'Liked videos' in word:
   device.say("Ok,opening Liked Videos on youtube")
   device.runAndWait()
   print("Opening Liked Videos on Youtube..")
   ytll = 'https://www.youtube.com/playlist?list=LL'
   webbrowser.open(ytll)
 if 'Netflix' in word:
   device.say("Ok,opening Netflix")
   device.runAndWait()
   print("Opening Netflix..")
   netflix = 'https://www.netflix.com/'
   webbrowser.open(netflix)
 if 'how do you pray' in word:
   device.say("Remove any negative thoughts from your mind and focus God only.")
   device.say("Feel free to talk to God about anything for he is your Father no matter what situation you are in.")
   device.say("You can tell him about your what you are facing or going through or you can thank him for what he has done in your life.")
   device.say("Remember ,with God, you have to exercise patience")
   device.runAndWait()
 if 'quit' in word or 'close app' in word:
   device.say("Ok, quitting..")
   device.runAndWait()
   quit()
 if 'restart' in word:
   device.say('Restarting computer')
   device.runAndWait()
   os.system("shutdown /r")
 if 'type' in word:
   word = str(word).replace('type','')
   device.say("Typing" + word)
   device.runAndWait()
   time.sleep(5)
   print("Type information:" + word)
   keyboard.write(word)
 if 'where is' in word:
   word = str(word).replace('where is','')
   device.say("Searching:" + word)
   device.runAndWait()
   print("Searching:" + word)
   results = wikipedia.summary(word,1)
   loc = 'https://www.google.com/search?q=' + word
   webbrowser.open(loc)
   device.say(results)
   device.runAndWait()
   print("Results:" + results)
 if "count from" in word:
   firstone = int(input("Enter the beginning number of the count: "))
   second = int(input("Enter the end number of the count: "))
   for count in range(firstone,second):
    device.say(count)
    device.runAndWait()
 if 'convert' in word: 
   device.say("Use terminal to convert the values")
   device.runAndWait()
   value1 = int(input("What value are you converting:"))
   unit1 = input("What is the value unit:")
   unit2 = input("What unit are you changing it to:")
   if unit1 == "kilometre" and unit2 == "metre":
    ans = value1*1000
    device.say("Answer is:" + str(ans) + "metres")
    device.runAndWait()
    print("Answer is:" + str(ans) + " metres")
   if unit1 == "metre" and unit2 == "kilometre":
    ans = value1/1000
    device.say("Answer is:" + str(ans) + "kilometres")
    device.runAndWait()
    print("Answer is:" + str(ans) + " kilometres")
   if unit1 == "grams" and unit2 == "kilograms":
    ans = value1/1000
    device.say("Answer is:" + str(ans) + "kilograms")
    device.runAndWait()
    print("Answer is:" + str(ans) + " kilograms")
   if unit1 == "kilograms" and unit2 == "grams":
    ans = value1*1000
    device.say("Answer is:" + str(ans) + "grams")
    device.runAndWait()
    print("Answer is:" + str(ans) + " grams")
 if 'switch Wi-Fi on' in word or 'switch on Wi-Fi' in word or 'turn on Wi-Fi' in word or 'turn Wi-Fi on' in word:
   device.say("Switching on Wi-Fi")
   device.runAndWait()
   print("Switching on Wi-Fi....")
   subprocess.run(["netsh","interface","set","interface","Wi-Fi","enabled"])
 if 'switch Wi-Fi off' in word or 'switch off Wi-Fi' in word or 'turn off Wi-Fi' in word or 'turn Wi-Fi off' in word:
   device.say("Switching off wifi")
   device.runAndWait()
   print("Switching off Wi-Fi....")
   subprocess.run(["netsh","interface","set","interface","Wi-Fi","disabled"])
 if 'search on YouTube' in word:
   word = str(word).replace("search on YouTube","")
   device.say("Searching on YouTube:" + word)
   device.runAndWait()
   print("Searching on YouTube:" + word)
   ytlink = "https://www.youtube.com/results?search_query=" + word
   webbrowser.open(ytlink)
 if 'find book called' in word:
   word = str(word).replace("find book called","")
   device.say("Scanning through the web")
   device.say("Yes,I found it")
   device.runAndWait()
   print("Opening website for your book")
   site = "https://b-ok.africa/s/" + word
   webbrowser.open(site)
 if 'encourage me' in word:
   device.say("Do you know you are a prince to Jesus Christ our lird and saviour")
   device.say("so don't be discouraged")
   device.runAndWait() 
 if 'speed up' in word:
   device.say("Increasing my car's speed")
   device.runAndWait()
   for speed in range(0,120):
     if speed == 60:
       device.say("Above speed limit which is 60 kilometres per hour")
       device.runAndWait()
       print("Above speed limit...")
       continue
     print("Speedometer:" + str(speed) + "Km/h")
 if "cmd" in word or "command prompt" in word or " Command prompt" in word:
   device.say("Opening Command Prompt...")
   device.runAndWait()
   print("Opening Command Prompt...")
   os.startfile("C:\\Users\\MrsZulu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk")
 if "Control Panel" in word or "control panel" in word:
   device.say("Opening Control Panel...")
   device.runAndWait()
   print("Opening Control Panel...")
   os.startfile("C:\\Users\\MrsZulu\\AppData\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk") 
 if "File Explorer" in word:
   device.say("Opening File Explorer...")
   device.runAndWait()
   print("Opening File Explorer...")
   os.startfile("C:\\Users\\MrsZulu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\File Explorer.lnk")
 if 'evil' in word:
   device.say("Sorry,I do not associate with such words")
   device.runAndWait()
 if 'is fasting important' in word:
   device.say("Fasting is very important for it helps you to connect more with God spiritually and to know more of him")
   device.say("Don't forget Jesus fasted for 40 days and 40 nights, so it is important to fast once in a while buut it depends on you")
   device.say("Don't forget to pray too, feel free to talk to God for he is waiting to listen to you")
   device.runAndWait()
 if 'create tab' in word:
   browser = webdriver.Chrome()
   link_tab = input("Enter url for your tab:")
   browser.get(link_tab)
   browser.execute_script('window.open("")')


def superbook():
   superlink = 'https://us-en.superbook.cbn.com/'
   device.say("Opening one of my favourite app websites of all time , Superbook")
   device.runAndWait()
   webbrowser.open(superlink)
def bible():
   bible = "https://www.bible.com/bible/59/GEN.1.ESV"
   device.say("Opening one of my favourite app websites of all time, the Bible")
   device.runAndWait()
   webbrowser.open(bible)
def aboutus():
   about = Tk()
   about.title("About Pixel")
   about.geometry("500x500")

   label = Label(about,text="About Us",font="23")
   label.pack()

   about.mainloop()
set = Menu(app)
toolbar = Menu(set, tearoff=0)
toolbar.add_command(label="About Us",command=aboutus)
toolbar.add_command(label="Superbook",command=superbook)
toolbar.add_command(label="Bible",command=bible)
toolbar.add_separator()
toolbar.add_command(label="Exit",command=app.quit)
set.add_cascade(label="File",menu= toolbar)

def voicechange():
  speaker = device.getProperty("voices")
  device.setProperty('voice',speaker[0].id)
  messagebox.showinfo('Messsage from Pixel:','Male voice has been activated')
def voicechangebeg():
  speaker = device.getProperty("voices")
  device.setProperty('voice',speaker[1].id)
  messagebox.showinfo('Messsage from Pixel:','Female voice has been activated')
def link():
  msg = 'C:/Users/MrsZulu/Documents/Programming/Assistance/Pixel.html'
  device.say("Use terminal to enter phone number of the receiver")
  device.runAndWait()
  tim = datetime.datetime.now()
  phonenumber = input("Enter phone number with country code: ")
  device.say("Please wait for link to be send...")
  device.runAndWait() 
  messagebox.showinfo('Messsage from Pixel:','Please wait for the duration presented on the terminal for link to be sent')
  pywhatkit.sendwhatmsg(phonenumber,msg,tim.hour,tim.minute+2,10)
  time.sleep(5)
def online():
  statusbtn = tk.Button(width="2",height="1",bg="green")
  statusbtn.pack(side="right")
  status = tk.Label(text="online")
  status.pack(side="right")
def offline():
  statusbtn = tk.Button(width="2",height="1",bg="grey")
  statusbtn.pack(side="right")
  status = tk.Label(text="offline")
  status.pack(side="right")
def busy():
  statusbtn = tk.Button(width="2",height="1",bg="orange")
  statusbtn.pack(side="right")
  status = tk.Label(text="busy")
  status.pack(side="right")
def sleep():
  statusbtn = tk.Button(width="2",height="1",bg="black")
  statusbtn.pack(side="right")
  status = tk.Label(text="Sleeping")
  status.pack(side="right")
set1 = Menu(app)
toolbar1 = Menu(set, tearoff=0)
toolbar1.add_command(label="Male voice",command=voicechange)
toolbar1.add_command(label="Female voice",command=voicechangebeg)
toolbar1.add_separator()
toolbar1.add_command(label="Exit",command=app.quit)
set.add_cascade(label="Edit",menu= toolbar1)
app.config(menu= set)
def quicknote():
  quick = Tk()
  quick.title("Quick note")
  quick.geometry("500x500")
  quick.iconbitmap('C:\\Users\\MrsZulu\\Documents\\Programming\\Assistance\\Pixelbg.ico')

  label1 = tk.Label(quick,text="Pixel's Quick Note",font="20")
  label1.pack()
  notebox = tk.Text(quick,width="55",height="15")
  notebox.pack()
  def enter1():
    content = notebox.get(1.0,'end')
    display.config(text=content)
  def clear1():
    notebox.delete(1.0,tk.END)
  def clear2():
    display.config(text="")
  enter = tk.Button(quick,text="Enter",width="20",height="3",bg="#06FB5C",command=enter1)
  enter.pack()
  clear = tk.Button(quick,text="Clear",width="20",height="3",bg="#F33711",command=clear1)
  clear.pack()
  delet = tk.Button(quick,text="Delete Note",width="20",height="3",bg="#11F3C0",command=clear2)
  delet.pack()
  label2 = tk.Label(quick,text="--Note display--",font="17")
  label2.pack()
  display = tk.Label(quick,text="",font="19")
  display.pack()
  quick.mainloop()
def RPC():
 r = Tk()
 r.title("Rock Paper Scissors game")
 r.geometry("")
 r.iconbitmap('C:\\Users\\MrsZulu\\Documents\\Programming\\Assistance\\Pixelbg.ico')

 set = Menu(r)
 toolbar = Menu(set, tearoff=0)
 toolbar.add_command(label="Back")
 toolbar.add_separator()
 toolbar.add_command(label="Exit",command=app.quit)
 set.add_cascade(label="File",menu= toolbar)

 r.config(menu= set)

 def rpc1():
    op = ['rock','paper','scissors']
    comans = random.choice(op)
    all = 'Computer Answer:' + comans
    computer.delete(1.0,tk.END)
    computer.insert(1.0,all)
    print(all)
    btn1 = 'rock'
    if comans == 'rock':
        computer.delete(1.0,tk.END)
        draw = "It is a draw.."
        computer.insert(1.0,draw)
        print("It is a draw")
    if comans == 'paper':
        computer.delete(1.0,tk.END)
        lose = "You lose.."
        computer.insert(1.0,lose)
        print("You lose..")
    if comans == 'scissors':
        computer.delete(1.0,tk.END)
        win = "You win.."
        computer.insert(1.0,win)
        print("You win..")
 def rpc2():
    op = ['rock','paper','scissors']
    comans = random.choice(op)
    all = 'Computer Answer:' + comans
    computer.delete(1.0,tk.END)
    computer.insert(1.0,all)
    print(all)
    btn2 = 'paper'
    if comans == 'paper':
        computer.delete(1.0,tk.END)
        draw = "It is a draw.."
        computer.insert(1.0,draw)
        print("It is a draw")
    if comans == 'scissors':
        computer.delete(1.0,tk.END)
        lose = "You lose.."
        computer.insert(1.0,lose)
        print("You lose..")
    if comans == 'rock':
        computer.delete(1.0,tk.END)
        win = "You win.."
        computer.insert(1.0,win)
        print("You win..")
 def rpc3():
    op = ['rock','paper','scissors']
    comans =  random.choice(op)
    print(comans)
    all = 'Computer Answer:' + comans
    btn3 = 'scissors'
    computer.delete(1.0,tk.END)
    computer.insert(1.0,all)
    print(all)
    if comans == 'scissors':
        computer.delete(1.0,tk.END)
        draw = "It is a draw.."
        computer.insert(1.0,draw)
        print("It is a draw")
    if comans == 'rock':
        computer.delete(1.0,tk.END)
        lose = "You lose.."
        computer.insert(1.0,lose)
        print("You lose..")
    if comans == 'paper':
        computer.delete(1.0,tk.END)
        win = "You win.."
        computer.insert(1.0,win)
        print("You win..")
 text1 = tk.Label(r,text="Choose between Rock,Paper and Scissors",font="22")
 text1.pack()
 btn1 = tk.Button(r,text="Rock",font="20",width="20",height="7",command=rpc1)
 btn1.pack()
 btn2 = tk.Button(r,text="Paper",font="20",width="20",height="7",command=rpc2)
 btn2.pack()
 btn3 = tk.Button(r,text="Scissors",font="20",width="20",height="7",command=rpc3)
 btn3.pack()
 computer = tk.Text(r,font="19",width="45",height="4")
 computer.pack()
 r.mainloop()
def ide():
 il = Tk()
 il.title("Pixel IDE")
 il.iconbitmap('C:\\Users\\MrsZulu\\Documents\\Programming\\Assistance\\Pixelbg.ico')

 fileloc = ""
 def filel(openfilesave):
     global fileloc
     fileloc = openfilesave
 def saveas():
     if fileloc == "":
      openfilesave = asksaveasfilename(filetypes=[("Python Files","*py")])
     else:
      openfilesave = fileloc  
     with open(openfilesave,'w') as fileopen:
      contxt = codebox.get(1.0,END)
      fileopen.write(contxt)
      filel(openfilesave)
     def openfile(): 
      openfilesave = askopenfilename(filetypes=[("Python files","*py")])
      with open(openfilesave,'r') as fileopen:
       content = fileopen.read()
       codebox.delete(1.0,END)
       codebox.insert(1.0,content)
       filel(openfilesave)

     set = Menu(app)
     toolbar = Menu(set, tearoff=0)
     toolbar.add_command(label="Open file",command=openfile)
     toolbar.add_command(label="Save",command=saveas)
     toolbar.add_command(label="Save As",command=saveas)
     toolbar.add_separator()
     toolbar.add_command(label="Exit",command=app.quit)
     set.add_cascade(label="File",menu= toolbar)
     il.config(menu= set)

     codebox = Text()
     codebox.pack()
     def place():
      codebox.delete(1.0,END)
      direct = ">>"
      codebox.insert(1.0,direct + "\n")
     def process():
      label = Label(il,text="Output")
      label.pack()
      outshow = Text(il,height="13")
      outshow.pack()
      loc = f"python{fileloc}"
      processer = subprocess.Popen(loc,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
      show,error = processer.communicate()
      outshow.insert(1.0,show)
      outshow.insert(1.0,error)
      run = Button(text="Run",width="25",height="2",command=process)
      run.pack()

     il.mainloop() 
 def openfile(): 
  openfilesave = askopenfilename(filetypes=[("Python files","*py")])
  with open(openfilesave,'r') as fileopen:
   content = fileopen.read()
   codebox.delete(1.0,END)
   codebox.insert(1.0,content)
   filel(openfilesave)

 set = Menu(il)
 toolbar = Menu(set, tearoff=0)
 toolbar.add_command(label="Open file",command=openfile)
 toolbar.add_command(label="Save",command=saveas)
 toolbar.add_command(label="Save As",command=saveas)
 toolbar.add_separator()
 toolbar.add_command(label="Exit",command=app.quit)
 set.add_cascade(label="File",menu= toolbar)
 il.config(menu= set)

 codebox = Text(il)
 codebox.pack()
 def place():
  codebox.delete(1.0,END)
  direct = ">>"
  codebox.insert(1.0,direct + "\n")
 def process():
  label = Label(il,text="Output")
  label.pack()
  outshow = Text(il,height="13")
  outshow.pack()
  loc = f"python{fileloc}"
  processer = subprocess.Popen(loc,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
  show,error = processer.communicate()
  outshow.insert(1.0,show)
  outshow.insert(1.0,error)
 run = Button(il,text="Run",width="25",height="2",command=process) 
 run.pack()
 il.mainloop()
def ytsearch():
 yt = Tk()
 yt.title("Youtube Searcher")
 yt.geometry("400x400")
 yt.iconbitmap('C:\\Users\\MrsZulu\\Documents\\Programming\\Assistance\\Pixelbg.ico')
 
 searchtext = Label(yt,text="YouTube Searcher",font="26")
 searchtext.pack()
 searcher = Entry(yt,width="60")
 searcher.pack()
 def search():
   content1 = searcher.get()
   ytlink = "https://www.youtube.com/results?search_query=" + content1
   webbrowser.open(ytlink)
 searchbtn = Button(yt,text="Search",command=search,width="20",height="2")
 searchbtn.pack()
 yt.mainloop()
set2 = Menu(app)
toolbar2 = Menu(set, tearoff=0)
toolbar2.add_command(label="Rock Paper Scissors",command=RPC)
toolbar2.add_command(label="Quick Note",command=quicknote)
toolbar2.add_command(label="IDE",command=ide)
toolbar2.add_command(label="Youtube Searcher",command=ytsearch)
toolbar2.add_separator() 
toolbar2.add_command(label="Exit",command=app.quit)
set.add_cascade(label="Apps",menu= toolbar2)
app.config(menu= set)

set3 = Menu(app)
toolbar3 = Menu(set, tearoff=0)
toolbar3.add_command(label="Whatsapp",command=link)
toolbar3.add_command(label="Facebook")
toolbar3.add_separator()
toolbar3.add_command(label="Exit",command=app.quit)
set.add_cascade(label="Share",menu= toolbar3)
app.config(menu= set)

set4 = Menu(app)
toolbar4 = Menu(set, tearoff=0)
toolbar4.add_command(label="Online",command=online)
toolbar4.add_command(label="Offline",command=offline)
toolbar4.add_command(label="Busy",command=busy)
toolbar4.add_command(label="Sleeping",command=sleep)
toolbar4.add_separator()
toolbar4.add_command(label="Clear",command="")
toolbar4.add_command(label="Exit",command=app.quit)
set.add_cascade(label="Status",menu= toolbar4)
app.config(menu= set)

def blue():
  app.configure(bg="#1D9BF8")
  text2.configure(bg="#1D9BF8")
  text3.configure(bg="#1D9BF8")
  text4.configure(bg="#1D9BF8")
  time1.configure(bg="#1D9BF8")
def green():
  app.configure(bg="#3AEF5A")
  text2.configure(bg="#3AEF5A")
  text3.configure(bg="#3AEF5A")
  text4.configure(bg="#3AEF5A")
  time1.configure(bg="#3AEF5A")
def purple():
  app.configure(bg="#9B0CED")
  text2.configure(bg="#9B0CED")
  text3.configure(bg="#9B0CED")
  text4.configure(bg="#9B0CED")
  time1.configure(bg="#9B0CED")
def orange():
  app.configure(bg="#F39C12")
  text2.configure(bg="#F39C12")
  text3.configure(bg="#F39C12")
  text4.configure(bg="#F39C12")
  time1.configure(bg="#F39C12")
def white():
  app.configure(bg="#FDFEFE")
  text2.configure(bg="#FDFEFE")
  text3.configure(bg="#FDFEFE")
  text4.configure(bg="#FDFEFE")
  time1.configure(bg="#FDFEFE")
def grey():
  app.configure(bg="#B3B6B7")
  text2.configure(bg="#B3B6B7")
  text3.configure(bg="#B3B6B7")
  text4.configure(bg="#B3B6B7")
  time1.configure(bg="#B3B6B7")
def yellow():
  app.configure(bg="#EBFF41")
  text2.configure(bg="#EBFF41")
  text3.configure(bg="#EBFF41")
  text4.configure(bg="#EBFF41")
  time1.configure(bg="#EBFF41")

set5 = Menu(app)
toolbar5 = Menu(set, tearoff=0)
toolbar5.add_command(label="Blue",command=blue)
toolbar5.add_command(label="Green",command=green)
toolbar5.add_command(label="Purple",command=purple)
toolbar5.add_command(label="Orange",command=orange)
toolbar5.add_command(label="White",command=white)
toolbar5.add_command(label="Grey",command=grey)
toolbar5.add_command(label="Yellow",command=yellow)
toolbar5.add_separator()
toolbar5.add_command(label="Exit",command=app.quit)
set.add_cascade(label="Background",menu= toolbar5)
app.config(menu= set)

app.config()

tog2 = ImageTk.PhotoImage(Image.open("C:\\Users\\MrsZulu\\Documents\\Programming\\Assistance\\cancel2.png"))
def toogle(): 
   space = Frame(app,width="150",height="1000",bg="#10E8CB")
   space.place(x=0,y=0)
   def calc():
    calc = Tk()
    calc.title("Pixel Calculator")

    display = Text(calc,width="80",height="4")
    display.grid(row="0",column="0",columnspan=5)
    #function
    def x():
     display.insert(1.0,"*")
    def div():
     display.insert(1.0,"/")
    def add():
     display.insert(1.0,"+")
    def minus():
     display.insert(1.0,"-")
    def clear():
     display.delete(1.0,END)
    def one():
     display.insert(1.0,"1")
    def two():
     display.insert(1.0,"2")
    def three():
     display.insert(1.0,"3")
    def four():
     display.insert(1.0,"4")
    def five():
     display.insert(1.0,"5")
    def six():
     display.insert(1.0,"6")
    def seven():
     display.insert(1.0,"7")
    def eight():
     display.insert(1.0,"8")
    def nine():
     display.insert(1.0,"9")
    def zero():
     display.insert(1.0,"0")
    def equal():
     fun = display.get(1.0,END)
     global ans
     try:
      ans = str(eval(fun))
      display.delete(1.0,"end")
      display.insert(1.0,ans)
     except:
      ans = ""
      display.delete(1.0,"end")
      display.insert(1.0,">>MATH ERROR")
    #row 1
    btn = Button(calc,text="X",width="20",height="2",command=x)
    btn.grid(row="1",column="1")
    btn1 = Button(calc,text="/",width="20",height="2",command=div)
    btn1.grid(row="1",column="2")
    btn2 = Button(calc,text="+",width="20",height="2",command=add)
    btn2.grid(row="1",column="3")
    btn3 = Button(calc,text="-",width="20",height="2",command=minus)
    btn3.grid(row="1",column="4") 
    #row2
    btn5 = Button(calc,text="C",width="20",height="2",command=clear)
    btn5.grid(row="2",column="1")
    btn6 = Button(calc,text="1",width="20",height="2",command=one)
    btn6.grid(row="2",column="2")
    btn7 = Button(calc,text="2",width="20",height="2",command=two)
    btn7.grid(row="2",column="3")
    btn8 = Button(calc,text="3",width="20",height="2",command=three)
    btn8.grid(row="2",column="4")
    #row 3
    btn9 = Button(calc,text="4",width="20",height="2",command=four)
    btn9.grid(row="3",column="1")
    btn10 = Button(calc,text="5",width="20",height="2",command=five)
    btn10.grid(row="3",column="2")
    btn11 = Button(calc,text="6",width="20",height="2",command=six)
    btn11.grid(row="3",column="3")
    btn12 = Button(calc,text="7",width="20",height="2",command=seven)
    btn12.grid(row="3",column="4")
    #row4
    btn13 = Button(calc,text="8",width="20",height="2",command=eight)
    btn13.grid(row="4",column="1")
    btn14 = Button(calc,text="9",width="20",height="2",command=nine)
    btn14.grid(row="4",column="2")
    btn15 = Button(calc,text="0",width="20",height="2",command=zero)
    btn15.grid(row="4",column="3")
    btn16 = Button(calc,text="=",width="20",height="2",command=equal)
    btn16.grid(row="4",column="3")
    calc.mainloop()
   btn1 = Button(app,text="Calculator",border=0,width="20",height="2",command=calc)
   btn1.place(x=0,y=50)
   def alarmapp():
    alarm = Tk()

    alarm.title("Pixel Alarm")
    alarm.geometry("400x400")

    title = Label(alarm,text="Set hour for alarm:")
    title.pack()
    hour = Entry(alarm,width="85")
    hour.pack()
    title1 = Label(alarm,text="Set minutes for alarm:")
    title1.pack()
    minute = Entry(alarm,width="85")
    minute.pack()
    title2 = Label(alarm,text="AM/PM:")
    title2.pack()
    ampm = Entry(alarm,width="85")
    ampm.pack()

    def stopbtn():
     stopbutton.destroy()
    def alarmset():
     hourtime = hour.get()
     minutetime = minute.get()
     ampmtime = ampm.get()
     currenttime = datetime.datetime.now()
     if ampmtime == "AM" and hourtime == 12:
          hourtime -= 12
     if ampmtime == "PM":
          hourtime += 12
     print("Alarm time:",str(hourtime) + ":" + str(minutetime),str(ampmtime))
     currenttime1 = currenttime.hour
     currenttime2 = currenttime.minute
     currenttime3 = currenttime.strftime("%p")
     print("Current time:",str(currenttime1) + ":" + str(currenttime2),str(currenttime3))

     while True:
      if datetime.datetime.now().hour == int(hourtime) and datetime.datetime.now().minute == int(minutetime):
         print("Wake up...")
         os.system("C:\\Users\\MrsZulu\\Documents\\Programming\\Assistance\\ChocolateCookieJam.mp3")
         global stopbutton
         stopbutton =  Button(alarm,text="Stop Alarm",width="25",height="2",command=stopbtn)
         stopbutton.pack()
         break
     settime = Button(alarm,text="Set Alarm",width="25",height="2",command=alarmset)
     settime.pack()


     alarm.mainloop()
   btn2 = Button(app,text="Alarm",border=0,width="20",height="2",command=alarmapp)
   btn2.place(x=0,y=100)
   def remove():
      space.destroy()
      btn.destroy() 
      btn1.destroy()
      btn2.destroy()
   btn = Button(app,image=tog2,activebackground="#10E8CB",bg="#10E8CB",border=0,command=remove)
   btn.place(x=0,y=0)
tog = ImageTk.PhotoImage(Image.open("C:\\Users\\MrsZulu\\Documents\\Programming\\Assistance\\toogle2.png"))
abtn =Button(app,image=tog,border=0,command=toogle)
abtn.place(x=0,y=0)

def tim():
  clock = time.strftime('%H:%M:%S')
  time1.config(text=clock)
  time1.after(200,tim)
time1 = tk.Label(text="",font='19',fg='blue')
time1.pack()
tim()
text2 = tk.Label(text="Press the button to start speaking to Pixel",font="20")
text2.pack()
start = tk.Button(text="Pixel",width="50",height="18",command=pixel,borderwidth=1,background='#1AEDCA')
start.pack()
text4 = tk.Label(text="--Your command--",font="15")
text4.pack()
text3 = tk.Label(text='')
text3.pack()  

messagebox.showinfo("Information from Pixel","When you are running Pixel,do not drag the GUI for it will stop functioning.")
device.say("Welcome to the Pixel app")
device.runAndWait()

app.mainloop()
#other sports scores
#update bible verses
#extract text from image
#alarm
#who sang the song
#brightness
#Sending email
#whatsapp
#show images
#tell me something about
#opening files
#audiobooks
#slideshow
#timer
#online status bar
#rename files
#subscribers
#football matches
#go to
#schedule
#youtube subscribers