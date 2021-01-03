"""Set of integrations tests"""

import pathlib

import click.testing
import pytest

from medicus_politicus import main


@pytest.fixture
def pdf_integration_test() -> pathlib.Path:
    """Path to the integration test .pdf file."""
    return pathlib.Path('./file_fixtures/integration_test.pdf')


@pytest.fixture
def substitutions_integrations_test() -> pathlib.Path:
    """Path to the integration substitutions .csv file."""
    return pathlib.Path('./file_fixtures/integration_substitutions.csv')


def test_sostituisci_exit_code(
        pdf_integration_test, substitutions_integrations_test
):
    runner = click.testing.CliRunner()

    # run the CLI with command "sostituisci"
    result = runner.invoke(
        main.sostituisci,
        [
            f"--file-pdf={pdf_integration_test}",
            f"--file-sostituzioni={substitutions_integrations_test}",
        ]
    )

    # remove the output file
    pathlib.Path('./file_fixtures/result.txt').unlink()

    assert result.exit_code == 0


def test_sostituisci_file_content(
        pdf_integration_test, substitutions_integrations_test
):
    runner = click.testing.CliRunner()

    # run the CLI with command "sostituisci"
    runner.invoke(
        main.sostituisci,
        [
            f"--file-pdf={pdf_integration_test}",
            f"--file-sostituzioni={substitutions_integrations_test}",
        ]
    )

    expected_content = 'This is the story of the Cow Hillary\n' \
                       'Dead the miaow, end of the story.'
    real_content = pathlib.Path('./file_fixtures/result.txt').read_text()

    # remove the output file
    pathlib.Path('./file_fixtures/result.txt').unlink()

    assert real_content.strip() == expected_content


def test_sostituisci_file_name(
        pdf_integration_test, substitutions_integrations_test
):
    runner = click.testing.CliRunner()

    # run the CLI with command "sostituisci"
    runner.invoke(
        main.sostituisci,
        [
            f"--file-pdf={pdf_integration_test}",
            f"--file-sostituzioni={substitutions_integrations_test}",
            "--nome-output=output"
        ]
    )

    output_file = list(pathlib.Path('./file_fixtures').glob('*.txt'))

    # remove the output file
    pathlib.Path('./file_fixtures/output.txt').unlink()

    assert len(output_file) == 1
    assert output_file[0].name == 'output.txt'
