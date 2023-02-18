import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

def voice_text():
    a = sr.Recognizer()
    with sr.Microphone() as b:
        print("The program is activated to excute your command........")
        a.adjust_for_ambient_noise(b)
        audio = a.listen(b)
        try:
            convarted_data = a.recognize_google(audio)
            #print("your data: ",convarted_data)
            return convarted_data
        except sr.UnknownValueError:
            print("sorry, your commound is not capture check your internet connection")


def text_voice(x):
    c = pyttsx3.init()
    voices = c.getProperty("voices")
    c.setProperty("voice", voices[1].id)
    rate = c.getProperty("rate")
    c.setProperty("rate", 150)
    c.say(x)
    c.runAndWait()
#text_voice()    

if __name__ == '__main__':
    if voice_text() == "hello":

     while True:
        data_1 = voice_text()
        print("your cammond is:", data_1)
        if "your name" in data_1:
            name = "my name is younha"
            text_voice(name)
        elif "can you hear me" in data_1:
            hear = ("Yes i can here you, what's your command")
            text_voice(hear)
        elif "old are you" in data_1:
            old = "i'm 2 years old"
            text_voice(old)
        elif "what's the  time" in data_1:
            time = datetime.datetime.now().strftime("%I%M%P")
            text_voice(time)
        elif "youtube" in data_1:
            text_voice("Opening youtube....")
            webbrowser.open("www.youtube.com")    
        elif "play song" in data_1:
            add = "D:\MUsic"
            listofvideo = os.listdir(add)
            print(listofvideo)
            os.startfile(os.path.join(add, listofvideo[1]))
        elif "exit" in data_1:
            text_voice("Thank you, Have a nice time")
            break
    else:
        print("not recognize")    