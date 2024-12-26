import random
import pyttsx3
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
import os
import wave

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.language = 'ru'

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Слушаю...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source)
            try:
                if self.language == 'en':
                    text = self.recognizer.recognize_google(audio, language='en-US')
                else:
                    text = self.recognizer.recognize_google(audio, language='ru-RU')
                print(f"Вы сказали: {text}")
                return text.lower()
            except sr.UnknownValueError:
                print("Извините, я не понял.")
                self.speak("Извините, я не понял.")
                return None
            except sr.RequestError as e:
                print(f"Проблема с подключением: {e}")
                self.speak("Проблема с подключением. Попробуйте позже.")
                return None

    def toss_coin(self):
        result = random.choice(['орел', 'решка'])
        self.speak(f"Выпало {result}.")

    def change_language(self):
        self.language = 'ru' if self.language == 'en' else 'en'
        self.speak("Язык изменён.")

    def start(self):
        self.speak("Здравствуйте! Я ваш голосовой ассистент Гена")
        while True:
            command = self.recognize_speech()
            if command:
                if 'монетку' in command or 'coin' in command:
                    self.toss_coin()
                elif 'пока' in command or 'bye' in command:
                    self.speak("До свидания!")
                    break
                elif 'язык' in command or 'language' in command:
                    self.change_language()
                elif 'привет' in command or 'hello' in command:
                    self.speak("Здравствуйте! Чем могу помочь?")
                else:
                    self.speak(f"Вы сказали: {command}")

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.start()
