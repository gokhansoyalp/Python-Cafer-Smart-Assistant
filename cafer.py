import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[2].id)
 
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Günaydın")
 
    elif hour>=12 and hour<18:
        speak("İyi günler")   
 
    else:
        speak("İyi akşamlar")  
 
    speak("Ben Cafer sana nasıl yardımcı olabilirim")       
 
def takeCommand():
    #It takes microphone input from the user and returns string output
 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        r.pause_threshold = 1
        audio = r.listen(source)
 
    try:
        print("Tanımlanıyor...")    
        query = r.recognize_google(audio, language='tr-TR')
        print(f"Komut: {query}\n")
        
 
    except Exception as e:
        # print(e)    
        print("Lütfen tekrar ediniz.")
        return "None"
    return query
 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
 
if __name__ == "__main__":
    while True:
    # if 1:
        query = takeCommand().lower()
 
    
        if 'cafer' in query:
            wishMe()
    
    
        elif 'araştırma yap' in query:
            speak('Neyi araştırmak istiyorsun ?')
            query = takeCommand()
            speak('Wikipedia da aranıyor...')
            wikipedia.set_lang('tr')
            results = wikipedia.summary(query)
            speak("Wikipedia ya göre...")
            print(results)
            speak(results)
 
        elif 'youtube oynatma listemi aç' in query:
            webbrowser.open("https://www.youtube.com")
 
        elif 'google aç' in query:
            webbrowser.open("google.com")
 
        elif 'stackoverflow aç' in query:
            webbrowser.open("stackoverflow.com")
            
            
        elif 'fenerbahçe maçını aç' in query:
            speak("Başarılar Fenerbahcem")
            webbrowser.open("https://beinsports.com.tr")
    
 
 
        elif 'Favori şarkımı aç' in query:
            speak("Açıyorum")
            music_dir = 'C:\\Users\\user\\Desktop\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
            
        elif 'selam cafer' in query:
            speak("selam nasılsın, çoluk çocuk nasıl, evdekilere selam")
            speak("Ne yapmamı istersin.")
        
        elif 'cafer saat kaç' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"saat şu an {strTime}")
 
        elif 'vs kod aç' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
 
        elif 'email at' in query:
            try:
                speak("Kime atayım ?")
                content = takeCommand()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Dinliyorum...")
                    r.pause_threshold = 1
                    audio = r.listen(source)
                to = query = r.recognize_google(audio, language='tr-TR')   
                sendEmail(to, content)
                speak("Email gönderildi!")
            except Exception as e:
                print(e)
                speak("Üzgünüm. Email gönderilirken bir hata oluştu.")