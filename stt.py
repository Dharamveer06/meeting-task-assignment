import whisper

def transcribe_audio(audio_path):
    print("Transcribing audio...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]
