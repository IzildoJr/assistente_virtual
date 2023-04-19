import speech_recognition as sr
import os

def ouvir_microfone():

    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)
        print('Diga alguma coisa: ')

        # Armazena o que foi dito em uma váriavel
        audio = microfone.listen(source)
    

    try:
        
        frase = microfone.recognize_google(audio,language='pt-BR')
    
        if 'navegador' in frase:
            os.system('start chrome.exe')

        elif 'Excel' in frase:
            os.system('start Excel.exe')
        

        print('Voce disse: '+ frase)
    
    except sr.UnknownValueError:
        print('Não entendi')

    return frase

ouvir_microfone()