import speech_recognition as sr

listener = sr.Recognizer()
def listen():
    with sr.Microphone() as source:
        print('listening...')
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language='en-in')
        command = command.lower()
        print(command)

while True:
    listen()