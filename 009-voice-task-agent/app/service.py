from openai import APIError, AuthenticationError

from app.extract import extract_tasks
from app.transcribe import transcribe_audio


def run_pipeline(api_key: str, audio_file) -> tuple[str, list[str]]:
    try:
        transcript = transcribe_audio(api_key, audio_file)
        tasks = extract_tasks(api_key, transcript)
        return transcript, tasks
    except AuthenticationError as error:
        raise ValueError("Your OpenAI API key looks invalid.") from error
    except APIError as error:
        raise ValueError(f"OpenAI request failed: {error}") from error
