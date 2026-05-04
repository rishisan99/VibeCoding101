import json
from urllib.error import HTTPError
from urllib.request import Request
from urllib.request import urlopen

from feedback_intelligence_agent.core.schemas import AnalyzeResponse


def call_analyze_api(
    api_url: str,
    feedback: str,
    api_key: str,
) -> AnalyzeResponse:
    payload = json.dumps({"feedback": feedback, "api_key": api_key}).encode()
    request = Request(
        f"{api_url}/analyze",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request) as response:
            data = json.loads(response.read().decode())
    except HTTPError as error:
        body = error.read().decode()
        raise RuntimeError(body)
    return AnalyzeResponse.model_validate(data)
