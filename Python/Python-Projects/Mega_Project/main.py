import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary  # Make sure this module and its `music` dictionary are correctly set up.
import requests
from openai import OpenAI
import client
import openai

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# Fetch and speak news
def get_news():
    api_key = "f5dee95c54834b1c95ba19d9c90f7200"  # Replace with your NewsAPI key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    try:
        response = requests.get(url)
        news_data = response.json()

        if news_data["status"] == "ok":
            articles = news_data["articles"][:5]  # Fetch top 5 news headlines
            speak("Here are the top news headlines:")
            for i, article in enumerate(articles, 1):
                headline = article["title"]
                print(f"News {i}: {headline}")
                speak(f"News {i}: {headline}")
        else:
            speak("Sorry, I couldn't fetch the news.")
    except Exception as e:
        speak("An error occurred while fetching the news.")
        print(f"Error fetching news: {e}")

def Aiprocess(command):
#     client = OpenAI(api_key="pk-jzXUzkRGfoGgBSohhbXrYoSpuazgJvUBlAfUGStgQXiemaky")
#     completion = client.chat.completions.create(
#          model="gpt-3.5-turbo",
# messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             { "role": "user",
#                 "content":command }
#             ]
#     )
#     print(completion.choices[0].message.content)

# client code for deepseek api

       client = OpenAI(api_key="sk-2494c820a9dd448e868ec9973d3c2bb3", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)

 


# Process command function
def processCommand(c):
    c = c.lower()  # Normalize the command for case insensitivity
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        try:
            # Extract the song name
            song = c.split(" ", 1)[1]
            # Look up the song in the music library
            if song in musiclibrary.music:
                link = musiclibrary.music[song]
                speak(f"Playing {song}")
                webbrowser.open(link)
            else:
                speak(f"Sorry, I couldn't find the song '{song}' in your library.")
                print(f"Song '{song}' not found in the music library.")
        except IndexError:
            speak("Please specify a song to play.")
        except Exception as e:
            speak("An error occurred while trying to play the song.")
            print(f"An error occurred: {e}")
    
    
    elif "Tell me news" in c:
        speak("Fetching the latest news.")
        get_news()
    
    else:
        output=Aiprocess(c)
        speak(output)
    
# Main function
if __name__ == "__main__":
    speak("Initializing Alex...")

    recognizer = sr.Recognizer()

    while True:
        try:
            # Use microphone to listen for commands
            with sr.Microphone() as source:
                # Adjust for ambient noise
                print("Calibrating microphone...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening for the wake woAlex'...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                # Recognize the wake word
                word = recognizer.recognize_google(audio).lower()
                if word == "Alex":
                    speak("Yes, I am here!")
                    print("Alex Active. Listening for commands...")

                    # Listen for the actual command
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                        command = recognizer.recognize_google(audio)
                        print(f"Command received: {command}")

                        # Process the command
                        processCommand(command)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Request error from the speech recognition service: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


