import pyaudio
import soundfile as sf
import io
import numpy as np
from lameenc import Encoder
import keyboard  # For detecting spacebar press


def record_audio_until_spacebar(rate=44100, channels=1, chunk=1024):
    # Set up PyAudio for recording
    p = pyaudio.PyAudio()

    stream = p.open(
        format=pyaudio.paInt16,
        channels=channels,
        rate=rate,
        input=True,
        frames_per_buffer=chunk,
    )

    print("Recording... Press SPACEBAR to stop.")

    frames = []

    # Record audio until spacebar is pressed
    while not keyboard.is_pressed("space"):
        data = stream.read(chunk)
        frames.append(np.frombuffer(data, dtype=np.int16))

    print("Recording finished.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Convert frames to a NumPy array and write to WAV buffer
    wav_data = np.hstack(frames)

    wav_buffer = io.BytesIO()
    sf.write(wav_buffer, wav_data, rate, format="WAV", subtype="PCM_16")
    wav_buffer.seek(0)  # Move to the start of the buffer

    # Now encode to MP3 using lameenc
    encoder = Encoder()
    encoder.set_bit_rate(128)
    encoder.set_in_sample_rate(rate)
    encoder.set_channels(channels)
    encoder.set_quality(2)  # 2 = high quality

    mp3_buffer = io.BytesIO()
    mp3_data = encoder.encode(wav_data.tobytes())
    mp3_data += encoder.flush()
    mp3_buffer.write(mp3_data)
    mp3_buffer.seek(0)  # Move to the start of the buffer
    mp3_buffer.name = "record.mp3"

    return mp3_buffer


def save_buffer_to_file(buffer, file_name):
    # Open the file in binary write mode and write the buffer contents
    with open(file_name, "wb") as f:
        f.write(buffer.getbuffer())


def load_mp3_into_buffer(mp3_file_path: str) -> io.BytesIO:
    """
    Loads an MP3 file from disk into a BytesIO buffer.
    Args:
        mp3_file_path (str): Path to the MP3 file on disk.
    Returns:
        BytesIO: In-memory buffer containing MP3 file data.
    """
    with open(mp3_file_path, "rb") as f:
        audio_buffer = io.BytesIO(f.read())
    audio_buffer.name = mp3_file_path
    return audio_buffer


if __name__ == "__main__":
    # Example usage
    mp3_audio = record_audio_until_spacebar()  # Record until spacebar is pressed

    # Example usage to save the MP3 file
    save_buffer_to_file(mp3_audio, "output.mp3")
