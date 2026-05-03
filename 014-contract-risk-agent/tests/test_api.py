from unittest import TestCase, mock

from fastapi.testclient import TestClient

from api import app


class ApiTests(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.json(), {"status": "ok"})

    def test_analyze(self):
        data = {"risky_clauses": [], "missing_clauses": [], "inconsistencies": [], "cross_document_reasoning": [], "final_summary": "ok"}
        with mock.patch("api.analyze_contracts") as analyze:
            analyze.return_value.model_dump.return_value = data
            response = self.client.post("/analyze", data={"api_key": "sk-test"}, files=[("files", ("a.txt", b"one", "text/plain")), ("files", ("b.txt", b"two", "text/plain"))])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["final_summary"], "ok")
