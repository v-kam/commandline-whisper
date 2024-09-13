# Command Line Whisper
*Azure OpenAI Whisper Transcription Tool*

This project provides a command-line tool for running Azure OpenAI Whisper transcription. It allows you to record audio, transcribe it using Whisper, and copy the transcription to your clipboard. It's designed for ease of use in day-to-day work.

You will need your own Azure OpenAI Whisper endpoint to run it.

## Features

- Record audio from your microphone.
- Stop recording with a spacebar press.
- Transcribe the recorded audio using Azure OpenAI Whisper.
- Copy the transcription text to the clipboard.
- Simple command-line interface for ease of use.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the project root directory with the following parameters:

   ```env
   AZURE_OPENAI_ENDPOINT=<your-azure-openai-endpoint>
   AZURE_OPENAI_API_KEY=<your-azure-openai-api-key>
   WHISPER_DEPLOYMENT_NAME=<your-whisper-deployment-name>
   ```

   Replace `<your-azure-openai-endpoint>`, `<your-azure-openai-api-key>`, and `<your-whisper-deployment-name>` with your Azure OpenAI endpoint, API key, and deployment name.

## Usage

1. **Run the tool**:
   ```bash
   python app.py
   ```

2. **Follow the on-screen prompts**:
   - Press `ENTER` to start a new recording.
   - Press the `SPACEBAR` to stop recording.
   - The transcription will be printed to the console and copied to your clipboard.

3. **To exit the program**, use `CTRL+C`.
