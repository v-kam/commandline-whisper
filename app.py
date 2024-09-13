from io import BytesIO
from src.whisper import WhisperOpenAI
from src.record_audio import record_audio_until_spacebar
from dotenv import load_dotenv
import pyperclip  # For copying text to clipboard

# Load environment variables from .env file
assert load_dotenv()


def process_transcription():
    """
    Handles the recording, transcription, and clipboard copy process.
    """
    transciption_kwargs = {"language": "", "prompt": "", "temperature": 0.3}
    print(transciption_kwargs)

    while True:
        # Wait for user to press Enter to start a new recording or CTRL+C to exit
        input("\nPress ENTER to start a new recording or CTRL+C to exit.")

        # Record audio until spacebar is pressed
        audio_buffer:BytesIO = record_audio_until_spacebar()

        # Initialize the WhisperOpenAI class
        whisper = WhisperOpenAI()

        # Set transcription kwargs (optional)
        whisper.st_set_transcription_kwargs(**transciption_kwargs)

        # Transcribe the audio
        transcription_result = whisper.transcribe(audio_buffer)

        # Print the transcription result
        transcription_text = transcription_result["text"]
        print("Transcription Text:\n\n", transcription_text, "\n\n")
        print("Inference Duration:", transcription_result["inference_duration"], "seconds")

        # Copy transcription text to clipboard
        pyperclip.copy(transcription_text)
        print("Transcription copied to clipboard.")


if __name__ == "__main__":
    process_transcription()
