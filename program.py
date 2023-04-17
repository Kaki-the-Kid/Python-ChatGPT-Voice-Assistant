import openai
import pyttsx3
import speech_recognition as sr
import time

# Set you OpenAI API key
openai.api_key="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"

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:  
        return recognizer.recognize_google(audio)
    except:
        print("There was an error transcribing the audio to text")
    
def generate_response(prompt):
    response = openai.Completion.create(
      #engine="davinci",
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.6,
      #stop=["\n", " Human:", " AI:"]
      stop=None
    )
    return response["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
    
def main():
    while True:
        # Record audio
        print("Say Genius to start recording ...")
        
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcript = recognizer.recognize_google(audio)
                if transcript.lower == "genius":
                    # Record audio
                    filename = "input.wav"
                    print("Recording ...")
                    
                    with open("recording.wav", "wb") as source:
                        recognizer.adjust_for_ambient_noise(source)
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())
                            print("Done recording")
                            
                    # Transcribe audio to text
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print("Transcription: " + text)
                        
                    # Generate response using GPT-3
                    
                    
            except:
                print("There was an error recording the audio")
                        
            