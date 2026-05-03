from unittest import TestCase

from core.postprocess import clean_result
from models import AnalysisResult, InconsistencyItem


class PostprocessTests(TestCase):
    def test_inconsistency_dedupe_handles_contract_lists(self):
        result = AnalysisResult(
            inconsistencies=[
                InconsistencyItem(point="Termination", contracts=["a.txt", "b.txt"], reason="Different notice periods."),
                InconsistencyItem(point="Termination", contracts=["a.txt", "b.txt"], reason="Different notice periods."),
            ],
            final_summary="ok",
        )
        cleaned = clean_result(result)
        self.assertEqual(len(cleaned.inconsistencies), 1)
