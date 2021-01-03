"""
Main script to be run.

The idea is to run a CLI command like

.. code-block:: shell

    poetry run medicus_politicus sostituisci \
        --file nome_file.epub \
        --file-sostituzioni file_sostituzioni.txt \
        --output-name epub_sostituito.epub

"""


import pathlib
from typing import List, Tuple

import click
import click_pathlib
import pdfminer.high_level

from . import helpers


memoizer = helpers.Memoizer(cache_dir='./cache')


@click.group(
    help="Insieme di tool per digitalizzare la nostra umanità! "
         "Usa uno dei comandi qui sotto... "
         "Nel dubbio, scrivi il nome del comando seguito da --help"
)
def cli():
    """Implement the Command Line Interface."""
    pass


@memoizer.memoize()
def read_pdf(filepath: pathlib.Path) -> str:
    """Read a .pdf file"""
    text = pdfminer.high_level.extract_text(filepath)
    return text


@memoizer.memoize()
def read_substitutions(filepath: pathlib.Path) -> List[Tuple[str, str]]:
    """
    Read the file with the substitutions to perform.

    The file format is the following:

    ::

        original_string1|new_string1
        original_string2|new_string2
        ...


    :param filepath: path to the file to read.
    :return: List with the tuple (original_string,new_string)
    """
    # TODO: check for the file existence and that the file is a file

    # read the file as a text
    substitutions_str = filepath.read_text(encoding='utf-8')
    substitutions_list = substitutions_str.split('\n')
    substitutions = [
        tuple(sub.split('|'))
        for sub in substitutions_list
    ]

    return substitutions


def perform_substitutions(
        text: str, substitutions: List[Tuple[str, str]]
) -> str:
    """
    Given a text and a list of substitutions to perform on that text,
    return the corrected version of the text.

    :param text: text to be corrected.
    :param substitutions: list of tuples (old_string, new_string).
    :return: text with substitutions applied.
    """
    for old_string, new_string in substitutions:
        text = text.replace(old_string, new_string)

    return text


@cli.command(
    help="Legge il testo di un file .pdf; "
         "legge un file .csv contenente le sostituzioni da effettuare; "
         "effettua le sostituzioni e salva il testo risultante in un .txt; "
         "il file viene salvato nella stessa cartella del file .pdf.\n"
         "ATTENZIONE: se è presente un file .txt con lo stesso nome, "
         "questo viene sovrascritto."
)
@click.option(
    "--file-pdf",
    required=True,
    type=click_pathlib.Path(exists=True),
    help="Percorso del file .pdf originale"
)
@click.option(
    "--file-sostituzioni",
    required=True,
    type=click_pathlib.Path(exists=True),
    help="File .csv con le sostituzioni da effettuare; "
         "il formato deve essere di questo tipo:\n"
         "stringa_vecchia|stringa_nuova"
)
@click.option(
    "--nome-output",
    default='result',
    show_default=True,
    help="Nome del file .txt risultante"
)
def sostituisci(
        file_pdf: pathlib.Path, file_sostituzioni: pathlib.Path,
        nome_output: str
) -> None:
    """
    Read a .pdf file and a substitutions .csv file;
    perform the substitutions and then save the text in a .txt file.
    
    :param file_pdf: name of the .pdf input file.
    :param file_sostituzioni: name of the .csv input file with substitutions.
    :param nome_output: name of the .txt output file.
    :return: None.
    """
    # read the text in the .pdf file
    pdf = read_pdf(file_pdf)
    # read the .txt substitutions file
    substitutions = read_substitutions(file_sostituzioni)
    # perform the substitutions
    f_substituted = perform_substitutions(pdf, substitutions)
    # save the file
    output_filepath = file_pdf.with_name(nome_output + '.txt')
    output_filepath.write_text(data=f_substituted, encoding='utf-8')


if __name__ == '__main__':
    cli()
