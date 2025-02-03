import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Set up the microphone
with sr.Microphone() as source:
    print("Hello, I am your translator. Let's start")
    print("Adjusting for ambient noise... Please wait.")
    
    # Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source) 
    print("Listening for your command...")
    
    # Listen for speech
    audio = recognizer.listen(source)  

# Use Google Web Speech API to recognize speech
try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio, language="ur")
    print("You said: " + text)

except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")

except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
