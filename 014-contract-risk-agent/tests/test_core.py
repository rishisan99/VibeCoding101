from unittest import TestCase

from core.loader import load_contracts
from core.splitter import build_chunks
from core.validate import filter_docs, validate_files


class CoreTests(TestCase):
    def test_loader_and_splitter(self):
        docs = load_contracts([{"name": "a.txt", "content": b"first clause"}, {"name": "b.txt", "content": b"second clause"}])
        self.assertEqual(len(build_chunks(docs)), 2)

    def test_validation(self):
        validate_files([{"name": "a.txt"}, {"name": "b.txt"}])
        docs = filter_docs([{"name": "a.txt", "text": "a"}, {"name": "b.txt", "text": "b"}])
        self.assertEqual(len(docs), 2)
