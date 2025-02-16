# GPT-3.5 Voice Assistant for Android with QPython

## Description

This project is a voice assistant based on **GPT-3.5** running on **QPython** on Android. It allows users to interact with an intelligent assistant that responds in French, using both voice recognition and text-to-speech to make the experience more interactive.

### Features
- Responds in French to all questions.
- Uses text-to-speech to read out the answers aloud.
- Integrated voice recognition for allowing users to ask questions orally.
- Monitors inactivity and prompts the user after 5 minutes of no interaction.
  
## Prerequisites

Before running this project, you need the following:

- **QPython** (Download from the Play Store or official [QPython website](https://www.qpython.com/)).
- **Access to the GPT API**: [Get free API Key](https://www.youtube.com/watch?v=LL4DE98h2uQ). 
- **`androidhelper` module** to interact with the Android system (text-to-speech, speech recognition).
- A **working internet connection** to interact with the GPT API.

## Installation

### Step 1: Install QPython
1. Download and install **QPython** from the Play Store or official website.
2. Open QPython and create a new Python script.

### Step 2: Install Necessary Modules
In QPython, you need to ensure that the following modules are installed:
- `androidhelper` : For speech synthesis and speech recognition.
- `APIGPT` : To interact with the GPT API.

Install these libraries through QPython’s terminal or package manager.

### Step 3: Create a File for the Project
1. Create a new Python file in QPython and copy the assistant’s source code (or the provided code above).
2. Add your GPT API key in the code.

### Step 4: Run the Script
Once the script is ready and configured, you can run it in QPython and start interacting with the voice assistant. You can either type your question or say "parler" to use the voice recognition.

## Usage

1. Launch the Python script.
2. You will be greeted by the voice assistant and prompted to ask a question.
3. If inactive for 5 minutes, the assistant will ask if you’re still there.
4. Type a question or say "parler" to use voice recognition.
5. The assistant will respond with a voice reply.

## Troubleshooting

- **Voice recognition error**: Ensure your microphone is working correctly and that the necessary permissions are granted to QPython.
- **GPT API connection error**: Check your internet connection and the validity of your OpenAI API key.

## Contribution

If you wish to contribute to this project, you can:
1. Fork this repository.
2. Make your changes.
3. Create a **Pull Request** to propose your improvements.

## License

This project is licensed under the **MIT License**.

---

Thank you for using the **GPT-3.5 Voice Assistant**!
