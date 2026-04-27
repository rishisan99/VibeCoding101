from app.client import get_client
from app.models import TaskList


def extract_tasks(api_key: str, transcript: str) -> list[str]:
    client = get_client(api_key)
    response = client.responses.parse(
        model="gpt-4.1-mini",
        instructions="Extract only clear action items from the transcript.",
        input=transcript,
        text_format=TaskList,
    )
    data = response.output_parsed or TaskList(tasks=[])
    return [task.strip() for task in data.tasks if task.strip()]
