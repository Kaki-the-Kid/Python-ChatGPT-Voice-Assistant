# ChatGPT Voice Assistant made with Python

A simple Python voice assistant project that demonstrates text-to-speech, speech recognition, and OpenAI integration.

## Requirements

- Python 3.8 or newer
- `openai`
- `pyttsx3`
- `SpeechRecognition`

## Installation

1. Create and activate a virtual environment:

    python -m venv .venv
    source .venv/bin/activate

2. Install dependencies:

    pip install -r requirements.txt

3. Create a local `.env` file from the example and add your API key:

    cp .env.example .env

4. Update `.env` with your key:

    OPENAI_API_KEY="your_api_key_here"

   Or set the environment variable directly:

    export OPENAI_API_KEY="your_api_key_here"

## Usage

Run the main program:

    python program.py

## Libraries and dependencies

### OpenAI API

Install the OpenAI client:

    pip install openai

Get an API key at: [OpenAI - API keys](https://platform.openai.com/account/api-keys)

### pyttsx3

`pyttsx3` is a text-to-speech library that works offline and supports Python 2 and 3.

    pip install pyttsx3

Example:

```python
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
```

More info: [pyttsx3 GitHub page](https://github.com/nateshmbhat/pyttsx3)

### SpeechRecognition

Install SpeechRecognition:

    pip install SpeechRecognition

## Notes

- Danish speech support is a work in progress.
- This project is intended as a starter template for voice-enabled ChatGPT integration.

## References

* [YouTube - Create a ChatGPT Voice Assistant in 8 Minutes (Python Tutorial)](https://www.youtube.com/watch?v=8z8Cobsvc9k)
* [OpenAI API reference](https://platform.openai.com/docs/api-reference/introduction)
* [Pypi.org - pyttsx3](https://pypi.org/project/pyttsx3/)
