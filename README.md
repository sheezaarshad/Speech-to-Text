# Speech-to-Text Translator

## Overview

This project is a simple speech-to-text translator that converts spoken words into text using Python's `speech_recognition` library. The program listens to audio input from a microphone, processes the speech, and converts it into text using Google Web Speech API.

##

```bash
pip install speechrecognition
pip install pyaudio  # Required for microphone input
```

*Note:* If you face installation issues with `pyaudio`, install it manually using

```bash
python speech_to_text.py
```

### How It WorksFeatures

- Uses the `speech_recognition` library for speech processing.
- Captures audio input from the microphone.
- Adjusts for ambient noise to improve accuracy.
- Converts spoken Urdu speech into text using Google Web Speech API.
- Provides error handling for unrecognized speech and API request failures.

## Requirements

Ensure you have Python installed along with the necessary dependencies: the appropriate package for your system.

## Usage

Run the script to start the speech recognition process:

1. Initializes the speech recognizer.
2. Captures audio input from the microphone.
3. Adjusts for ambient noise for better recognition.
4. Processes the speech input and converts it into text.
5. Displays the recognized text in the console.


## Error Handling

- If the speech is not understood, it will return:\
  *"Sorry, I could not understand the audio."*
- If there is an issue with Google Speech API, it will display an error message.

