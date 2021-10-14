# author: @youssefkhalil320
# Date: 10/14/2021 
# you can fing a video for me explaning the library     https://www.youtube.com/watch?v=OZ_Eej53qiQ&t=29s

import easyocr                                      # the library responsible for OCR 
import pyttsx3                                      # the library responsible for converting text to speech 

engine = pyttsx3.init()                             
image_path = 'download.png'                         # reading the image path 
reader = easyocr.Reader(['en'], gpu = False)        # choosing the English language and telling the programe that we are not using GPU 
result = reader.readtext(image_path, detail = 0)    # reading the text and removing the location details 
data = ' '.join(result)                             # collecting all th words in One string           
print(' '.join(result))
text_file = open("extracted_data.txt", "w")         # creating a text file in the same directory 
n = text_file.write(data)                           # writing the data in this file 
text_file.close()                                   # closing the file 
engine.say(result)                                  #converting the text to speech 
engine.runAndWait()
print(n)