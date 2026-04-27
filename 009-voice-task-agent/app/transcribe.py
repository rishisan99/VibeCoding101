from app.client import get_client


def transcribe_audio(api_key: str, audio_file) -> str:
    client = get_client(api_key)
    audio_file.seek(0)
    text = client.audio.transcriptions.create(
        model="gpt-4o-mini-transcribe",
        file=audio_file,
        response_format="text",
    )
    return str(text).strip()
