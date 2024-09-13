import os
from openai import AzureOpenAI
import time
from io import BytesIO
from dotenv import load_dotenv

assert load_dotenv()


class WhisperOpenAI:
    def __init__(self, deployment_id: str = os.getenv("WHISPER_DEPLOYMENT_NAME")) -> None:
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-02-01",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )

        self.deployment_id = deployment_id  # This will correspond to the custom name you chose for your deployment when you deployed a model.

    def transcribe(self, audio_buffer: BytesIO, **transcription_kwargs) -> dict:
        """
        optional kwargs for the model:
        language: str | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        response_format: Literal["json", "text", "srt", "verbose_json", "vtt"] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        timestamp_granularities: List[Literal["word", "segment"]] | NotGiven = NOT_GIVEN,
        """
        audio_buffer.seek(0)  # reset the buffer

        start_time = time.perf_counter()
        transciption: str = self.client.audio.transcriptions.create(
            file=audio_buffer, model=self.deployment_id, **transcription_kwargs
        ).text

        end_time = time.perf_counter()

        # Calculate elapsed time
        elapsed_time = round(end_time - start_time, 2)

        return {
            "text":transciption,  # text of the transcription
            "inference_duration":elapsed_time,  # duration of the transcription process
        }
