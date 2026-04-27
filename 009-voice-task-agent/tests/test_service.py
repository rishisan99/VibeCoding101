import unittest
from unittest.mock import Mock, patch

from openai import AuthenticationError

from app.service import run_pipeline


class ServiceTests(unittest.TestCase):
    @patch("app.service.extract_tasks", return_value=["Call Sam"])
    @patch("app.service.transcribe_audio", return_value="Call Sam tomorrow")
    def test_run_pipeline(self, transcribe, extract):
        transcript, tasks = run_pipeline("key", object())
        self.assertEqual(transcript, "Call Sam tomorrow")
        self.assertEqual(tasks, ["Call Sam"])
        transcribe.assert_called_once()
        extract.assert_called_once()

    @patch("app.service.transcribe_audio")
    def test_invalid_key_message(self, transcribe):
        transcribe.side_effect = AuthenticationError(
            "bad key", response=Mock(request=object()), body=None
        )
        with self.assertRaises(ValueError) as error:
            run_pipeline("bad", object())
        self.assertIn("invalid", str(error.exception).lower())


if __name__ == "__main__":
    unittest.main()
