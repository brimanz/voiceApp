import speech_recognition as sr
import webbrowser
import pyttsx3

voice = sr.Recognizer()
engine = pyttsx3.init()


def talk():

	mic = sr.Microphone()
	with mic as source:

		audio = voice.listen(source)

	text = voice.recognize_google(audio, language="ES")

	print(f'Dijiste: {text}')
	return text.lower()

if 'amazon' in talk():

	engine.say('Que deseas comprar en Amazon')
	engine.runAndWait()
	text = talk()
	webbrowser.open(f'https://www.amazon.es/s?k={text}')