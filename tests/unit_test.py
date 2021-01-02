"""Here you find the unit tests."""

import pathlib

import pytest

from medicus_politicus import main


@pytest.fixture
def pdf_test() -> pathlib.Path:
    """Path to the test .pdf file."""
    return pathlib.Path('./file_fixtures/test.pdf')


@pytest.fixture
def substitutions_test() -> pathlib.Path:
    """Path to the test substitutions .csv file."""
    return pathlib.Path('./file_fixtures/substitutions.csv')


def test_read_pdf(pdf_test):
    text = main.read_pdf(pdf_test)

    assert text.strip() == 'Test test'


def test_read_substitutions(substitutions_test):
    substitutions = main.read_substitutions(substitutions_test)
    expected_substitutions = [
        ("old_string", "new_string"),
        ("very_old_string", "super_new_string")
    ]

    assert substitutions == expected_substitutions
