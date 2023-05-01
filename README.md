# ChatGPT Voice Assistant made with Python

I have come to love the tool tha AI assisted coding delivers. It doesn´t remove the need for knowing how to code. But the help from the AI expands the help functions we are come to expext from Intellicense in the diffenrent IDEs.

## Libraries and dependencies

### OpenAI API

Først install OpenAI API - pref. in a virtuel environment

    pip install openai

You canb get API ket free for personal use at: [OpenAI - API keys](https://platform.openai.com/account/api-keys)

### pyttsx3

From pypi.org:
pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

    pip install pyttsx3

An example of using pyttsx3

```python
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
```
You can find more on the [pyttsx3 GitHub page](https://github.com/nateshmbhat/pyttsx3)

## Install Speech Recognition

    pip install SpeechRecognition

## Making the program speak danish
[TODO]
* https://polygon.io/dashboard/api-keys/9cb778f0-a448-4871-b0a3-6af073fe67bb
* https://github.com/fnielsen/awesome-danish
* chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/http://www.imm.dtu.dk/~faan/ps/Nielsen2016Danish.pdf
* https://spacy.io/models/da or https://spacy.io/models
* spaCy Library Architecture - https://spacy.io/api
* https://melaniewalsh.github.io/Intro-Cultural-Analytics/05-Text-Analysis/Multilingual/Danish/03-POS-Keywords-Danish.html
* https://www.resemble.ai/danish-tts/

## References

* [YouTube - Create a ChatGPT Voice Assistant in 8 Minutes (Python Tutorial)](https://www.youtube.com/watch?v=8z8Cobsvc9k)
* [OpenAI API reference](https://platform.openai.com/docs/api-reference/introduction)
* [Pypi.org - pyttsx3 2.90](https://pypi.org/project/pyttsx3/)
