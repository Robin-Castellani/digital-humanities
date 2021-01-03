"""Here you find the unit tests."""

import pathlib

import medicus_politicus.functions
import pytest


@pytest.fixture
def pdf_test() -> pathlib.Path:
    """Path to the test .pdf file."""
    return pathlib.Path('./file_fixtures/test.pdf')


@pytest.fixture
def substitutions_test() -> pathlib.Path:
    """Path to the test substitutions .csv file."""
    return pathlib.Path('./file_fixtures/substitutions.csv')


def test_read_pdf(pdf_test):
    text = medicus_politicus.functions.read_pdf(pdf_test)

    assert text.strip() == 'Test test'


def test_read_substitutions(substitutions_test):
    substitutions = medicus_politicus.functions\
        .read_substitutions(substitutions_test)
    expected_substitutions = [
        ("old_string", "new_string"),
        ("very_old_string", "super_new_string")
    ]

    assert substitutions == expected_substitutions


def test_perform_substitutions():
    original_text = 'W rong str!ng, please,can you c0rr3ct me?'
    substitutions = [
        ('W rong', 'Wrong'),
        ('str!ng', 'string'),
        ('please,can', 'please, can'),
        ('c0rr3ct', 'correct')
    ]

    expected_text = 'Wrong string, please, can you correct me?'

    substituted_text = medicus_politicus.functions\
        .perform_substitutions(original_text, substitutions)

    assert substituted_text == expected_text
