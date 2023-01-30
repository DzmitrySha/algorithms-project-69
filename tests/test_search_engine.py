import pytest
from search_engine.search_engine import search


doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot shoot shoot that thing at me."
doc3 = "I'm your shooter."


@pytest.fixture
def docs():
    documents = [
        {'id': 'doc1', 'text': doc1},
        {'id': 'doc2', 'text': doc2},
        {'id': 'doc3', 'text': doc3},
    ]
    return documents


@pytest.fixture
def search_word():
    search_word = "shoot"
    return search_word


def test_search_engine(docs: list, search_word: str):
    assert search(docs, search_word) == ['doc1', 'doc2']
    assert search([], search_word) == []
    assert search(docs, "pint") == ['doc1']
