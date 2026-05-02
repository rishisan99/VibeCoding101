import unittest
from unittest.mock import Mock, patch

from requests import RequestException

from app.ui.client import request_plan


class ClientTests(unittest.TestCase):
    @patch("app.ui.client.requests.post")
    def test_request_plan_success(self, mock_post):
        mock_post.return_value = Mock(ok=True, json=lambda: {"research_plan": "plan"})
        data = request_plan("http://test", "AI agents", "key")
        self.assertEqual(data["research_plan"], "plan")

    @patch("app.ui.client.requests.post")
    def test_request_plan_error(self, mock_post):
        mock_post.return_value = Mock(ok=False, json=lambda: {"detail": "Bad key"})
        with self.assertRaisesRegex(RuntimeError, "Bad key"):
            request_plan("http://test", "AI agents", "key")

    @patch("app.ui.client.requests.post", side_effect=RequestException("boom"))
    def test_request_plan_network_error(self, _mock_post):
        with self.assertRaises(RuntimeError):
            request_plan("http://test", "AI agents", "key")
