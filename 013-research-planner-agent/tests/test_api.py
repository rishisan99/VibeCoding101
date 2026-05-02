import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from app.api.main import app

client = TestClient(app)


class ApiTests(unittest.TestCase):
    @patch("app.api.main.build_plan")
    def test_plan_success(self, mock_build_plan):
        mock_build_plan.return_value = {
            "research_plan": "plan",
            "search_questions": ["q1", "q2"],
            "source_strategy": "sources",
            "output_template": "template",
        }
        response = client.post("/plan", json={"topic": "AI agents", "api_key": "key"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("research_plan", response.json())

    def test_topic_required(self):
        response = client.post("/plan", json={"topic": "", "api_key": "key"})
        self.assertEqual(response.status_code, 422)

    def test_key_required(self):
        response = client.post("/plan", json={"topic": "AI agents", "api_key": ""})
        self.assertEqual(response.status_code, 422)
