from time import sleep

import pyttsx3 #pip install pyttsx3
import PyPDF2 #pip install PyPDF2

story = open('lucy.pdf', 'rb') #Name of your script make sure it's in pdf format
pdfReader = PyPDF2.PdfFileReader(story)
pages = pdfReader.numPages
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #For male voice change the value as

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()