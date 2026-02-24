from this import d
import pyttsx3 as ps
import speech_recognition as sr
import datetime
import webbrowser
import subprocess
import pyaudio
import wikipedia
import random
import googletrans
from googletrans import Translator
import os
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import sports
import pynotifier
from pynotifier import Notification
import pyautogui as pag
import psutil
import playsound
import time
import screen_brightness_control as sbc
import cv2
from flask import Flask, request
import pywhatkit

device = ps.init()
speaker = device.getProperty("voices")
device.setProperty('voice',speaker[1].id)
device.say("Hi my name is pixel,your personal assistant")
device.say("How may I help you?")
device.runAndWait()
audio = sr.Recognizer()
try:
 with sr.Microphone() as source: 
  device.say("Wait for a signal to speak")
  device.runAndWait()
  device.say("Speak now..")
  device.runAndWait()
  print("Speak now....")
  speech = audio.listen(source) 
  print("Recognizing")
  word = audio.recognize_google(speech,language="en-in")
  print("You said:" + word)
  device.say("Got it")
  device.runAndWait()
  print("Recognized your voice..")
except sr.UnknownValueError:
 device.say("Sorry,I did not get that")
 device.runAndWait()


Notification(
  title="Notification from Pixel",
  description = str(word),
  duration= 60
  ).send()
if 'YouTube' in word:
  device.say("Ok,opening youtube")
  device.runAndWait()
  print("Opening YouTube..")
  youtub = 'https://www.youtube.com/'
  webbrowser.open(youtub)
if 'good morning' in word:
  device.say("Good morning,I assume you are well")
  device.runAndWait()
if 'how are you' in word:
  device.say("I am fine sir,and I am delighted to assist you")
  device.runAndWait()
if 'time' in word:
  tim = datetime.datetime.now().strftime("%H %M %S")
  device.say("The time is: " + tim )
  device.runAndWait()
  print(tim)
if 'play Christian music' in word:
  print("Playing one of your favorite Christian music")
  device.say("Playing one of your favorite Christian music")
  device.runAndWait()
  salvpo = ['https://www.youtube.com/watch?v=Ln_hEVnsdWY',
            'https://www.youtube.com/watch?v=wRJZQFRyZ6s',
            'https://www.youtube.com/watch?v=sbOcVER0WqU',
            'https://www.youtube.com/watch?v=Ipl-rLRxOrs'
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
   minecraft = ''
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
  device.say("Searching")
  device.runAndWait()
  word = str(word).replace("search","")
  print("Searching:" + word)
  webbrowser.open(search + word)
if 'open Whatsapp' in word:
  device.say("Opening whatsapp..")
  device.runAndWait()
  print("Opening whatsapp..")
  whatspp = 'https://web.whatsapp.com/'
  webbrowser.open(whatspp)
if 'Wikipedia' in word:
  word = str(word).replace("Wikipedia","")
  wiki = ''
  print()
  device.say()
  device.runAndWait()
  webbrowser.open()
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
if 'play song called' in word:
  word = str(word).replace("play song called","")
  pl = 'https://www.youtube.com/results?search_query='
  device.say("Searching" + word)
  device.runAndWait()
  print("Playing " + word)
  webbrowser.open(pl + word)
if 'recommend me a password' in word:
  password = ["3245","3646","bhdw78793","3838","788309","hrkh3878","83838","0390208","847898","849058","98088","1398","lsldh99","763743","vvaxcg","agcsg57"]
  device.say("Recommend password is: " + random.choice(password))
  device.runAndWait()
if 'calculator' in word:
  device.say("Opening calculator..")
  device.runAndWait()
  print("Opening calculator..")
  zo ='C:\Windows\System32\calc.exe'
  os.startfile(zo)
if 'Gmail' in word:
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
if 'translate' in word:
  language = Translator()
  word = str(word).replace("translate","")
  lang = language.translate(word,src='en',dest='fr')
  device.say("Your tranlation is:"+ lang)
  device.runAndWait()
  print("Your tranlation is:" + lang)
if 'open My Playlist' in word:
  playlist = 'https://www.youtube.com/playlist?list=PLZDBPlF5-zx1Kj5clsFF-SPzI-0wH5tq0'
  device.say("Opening playlist on YouTube")
  device.runAndWait()
  print("Opening playlist on YouTube..")
  webbrowser.open(playlist)
if 'play my music' in word:
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
   word = 'calculate'+ ''
   word = word.replace('calculate','')
   device.say("Answer is: " + sum(int(word)))
   device.runAndWait()
   print("Answer is: " + sum(word))
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
if 'open zoom' in word:
  device.say("Opening Zoom..")
  device.runAndWait()
  print("Opening Zoom..")
  zoom =' '
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
if 'look up' in word:
  word = str(word).replace("look up","")
  search = 'https://www.google.com/search?q='
  device.say("Searching" + word)
  device.runAndWait()
  print("Searching:" + word)
  webbrowser.open(search + word)
  data = ''
  opend = BeautifulSoup()
if 'open file' in word:
  word = str(word).replace('open file','')
  device.say("Accessing files..")
  device.say("Opening file..")
  device.runAndWait()
  print("Opening " + word)
  filel = 'C:\\Users\\MrsZulu\\Desktop\\IGCSE past papers\\'
  os.startfile(filel + word + ".pdf")
if 'send email saying' in word:
  gmailserver = smtplib.SMTP_SSL("smtp.gmail.com",456)
  gmailserver.starttls()
  gmailserver.login('ndo5.create@gmail.com','ndopiwe3')
  gmailserver.sendmail("ndo5.create@gmail.com",
                       "chickenland119@gmail.com",
                       word)
  device.say("Sending email..")
  device.runAndWait()
  print("Sending email...")
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
if 'play baby music' in word:
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
if 'what is the' in word:
  search = 'https://www.google.com/search?q='
  device.say("Searching" + word)
  device.runAndWait()
  print("Searching:" + word)
  webbrowser.open(search + word)
if 'remind me at' in word:
  word = str(word).replace('remind me at to','')
  tim = str(time.time() + word)
  while True:
   if time.time() == tim in word: 
    device.say("Setting reminder at:"+ word)
    device.runAndWait()
    print("Setting reminder at:"+ word)
if 'Google translate' in word:
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
  device.say("I like to practice my voice getting ready for work")
  device.say("Then get to work until I knock off.")
  device.runAndWait()
if 'how do you stay busy' in word:
  device.say("I do something productive each day")
  device.say("As they say an idle mind is the devil's workshop that why you should always up and running")
  device.runAndWait()
if 'can you speak some Italian' in word:
  device.say("")
  device.runAndWait()
if 'what is your favorite thing on the internet' in word:
  device.say("I like research so that I am more educated")
  device.runAndWait()
if 'what makes me happy' in word:
  device.say('I am always because Jesus brings me peace')
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
if 'sing me a birthday song' in word:
  device.say("")
  device.runAndWait()
if 'do you have a favorite colour' in word:
  device.say("My favorite colours are white and blue")
  device.runAndWait()
if 'can you do my homework' in word:
  device.say("Ok just tell me to search the question but if it is a test that is cheating")
  device.runAndWait()
if 'thank you' in word:
   device.say("you are most welcome, I am Happy to make an impact")
   device.runAndWait()
if 'open Notepad' in word:
   device.say("Opening notepad")
   device.runAndWait()
   print("Opening notepad...")
   notepad = 'C:\\Windows\\System32\\notepad.exe'
   os.startfile(notepad)
if 'what subject do you like' in word:
   device.say("I love computer science for it is very fascinating")
   device.runAndWait()
if 'open Android Studio' in word:
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
if 'obs' in word:
   device.say("Opening Open broadcaster software")
   device.runAndWait()
   print("Opening Open broadcaster software")
   obs = 'C:\\Program Files (x86)\\obs-studio\\bin\\32bit\\obs32.exe'
   os.startfile(obs)
if 'save my exams' in word:
  sme = 'https://www.savemyexams.co.uk/igcse/'
  device.say("Opening save my exams")
  device.runAndWait()
  print("Opening save my exams..")
  webbrowser.open(sme)
if 'hi' in word:
   device.say("Hi, how was your day")
   device.runAndWait()
if 'I am good' in word:
   device.say("I am happy to hear that")
   device.runAndWait()
if 'It was good' in word:
   device.say("How wonderful")
   device.runAndWait
if 'how do you' in word:
   sea = 'https://www.google.com/search?q='
   device.say("Searching question")
   device.runAndWait()
   print("Searching question..")
   webbrowser.open(sea + word)
if 'decrease volume' in word:
   device.say("Ok, decreasing volume")
   device.runAndWait()
   print("decreasing volume..")
   pag.press("volumedown")
if 'increase volume' in word:
   device.say("Ok, increasing volume")
   device.runAndWait()
   print("increasing volume..")
   pag.press("volumeup")
if 'mute volume' in word:
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
   football = sports.get_sport(sports.FOOTBALL)
   device.say("The matches for today are: " + football)
   device.runAndWait()
   print(football)
if 'screenshot' in word:
   device.say("Taking screenshot..")
   device.say("Screenshot taken..")
   device.runAndWait()
   print("Screenshot taken..")
   x = "screenshot taken by Pixel"
   pag.screenshot("C:\\Users\\MrsZulu\\Pictures\\Screenshots\\" + str(x) + ".png")
   x += str(1)
if 'alarm' in word:
   times = str(word).replace("set alarm at","")
   localtime = datetime.datetime.now().strftime("%H %M")
   device.say("Setting alarm..")
   device.say("Alarm set..")
   device.runAndWait()
   print("Alarm set...")
if times == localtime:
     print("Wake up now...")
     playsound("Chocolate Cookie Jam - An Jone.mp3")
     device.say("Wake up now..")
     device.runAndWait()
if 'brightness' in word or 'set brightness at' in word:
   word = str(word).replace('set brightness at','')
   bright = sbc.get_brightness(word)
   device.say("setting brightness by" + word)
   device.runAndWait()
   print(bright)
if 'am I a good person' in word:
   device.say("Everyone is, It just depends on how you bring out your inner kindness and genorosity")
   device.runAndWait()
if 'pixel cam' in word or 'cam for pixel' in word or 'pixel webcam' in word:
   device.say("Opening Pixel webcam...")
   device.runAndWait()
   print("Opening Pixel webcam...")
   videocap = cv2.VideoCapture(0)
   while (True):
    ret, frame = videocap.read()
    cv2.imshow('Pixel webcam',frame)
    if cv2.waitKey(10) == ord('b'):
      break
    videocap.release()
    cv2.destroyAllWindows()
if 'who sang the song' in word:
  word = str(word).replace("who sang the song","")
  identify = 'https://www.google.com/' + word
  req = requests.get(identify)
  beau = BeautifulSoup(req.text,'html.parser')
  singer = beau.find()
  device.say("This is a song called:" + singer)
  device.runAndWait()
  print("This is a song called:" + singer)
if 'date' in word:
  current = datetime.datetime.now()
  getdate = current.strftime("%d %m %y")
  device.say("The date is: " + getdate)
  device.runAndWait()
  print("The date is: " + getdate)
if 'send WhatsApp message' in word:
   device.say("Make sure you have a whatsapp browser")
   device.runAndWait()
   tim = datetime.datetime.now()
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
    pywhatkit.sendwhatmsg(phonenumber,word,tim.hour,tim.minute+2)
if 'how was your day' in word:
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
   device.say("Type email details using terminal..")
   device.runAndWait()
   sender = input("Enter email address using to send email: ")
   receiver = input("Enter email to whom you are sending to: ")
   password = input("Enter email password to login in: ")
   device.say("Say message for email")
   device.runAndWait()
   print("Say message for email..")
   with sr.Microphone() as source:
    try:
     print("Recognizing..")
     speech = audio.listen(source) 
     device.say("Recognizing voice..")
     device.runAndWait()
     audio.adjust_for_ambient_noise(source)
     word = audio.recognize_google(speech,language="en-in")
     print("Email Message : " + word)
     device.say("Got it")
     device.runAndWait()
    except:
     pass
    gmailserver = smtplib.SMTP_SSL("smtp.gmail.com",465)
    gmailserver.starttls()
    gmailserver.login(sender,password)
    gmailserver.sendmail(sender,
                       receiver,
                       word)
    device.say("Sending email...")
    device.runAndWait()
    print("Sending email...")
    device.say("email sent...")
    device.runAndWait()
    print("Email sent...")
  #birthday singing
  #what is the meaning of life 
  #love your ememies 
  #speaking languages
  #opening file
  #wikipedia problem
  #minecraft and zoom problem
  #live football score
  #send emails
  #reminder
  #open folders
  #open file
  #calculate
  #translate
  #open applicatoins
  #show me images of
  #programmed by Ndopiwe Zulu