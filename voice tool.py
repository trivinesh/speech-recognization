import speech_recognition as sr
import pywhatkit
import pyttsx3

# Create a speech recognition object
r = sr.Recognizer()

# Create a microphone object
mic = sr.Microphone()

# Define a function to process voice commands
def process_voice_command():
    engine = pyttsx3.init()  # Initialize the engine inside the function
    with mic as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        # Recognize the speech
        text = r.recognize_google(audio, language="en-US")
        print("You said: " + text)
        
        # Process the voice command
        if "search" in text:
            query = text.replace("search", "")
            pywhatkit.search(query)
        elif "play" in text:
            query = text.replace("play", "")
            pywhatkit.playonyt(query)
        elif "what is" in text:
            query = text.replace("what is", "")
            data = pywhatkit.info(query)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(data)
            engine.runAndWait()
        else:
            print("Sorry, I didn't understand that.")
    
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print("Error; {0}".format(e))

# Run the program
while True:
    process_voice_command()