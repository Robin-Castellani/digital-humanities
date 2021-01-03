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

import click
import click_pathlib
from medicus_politicus.functions import read_pdf, read_substitutions, \
    perform_substitutions

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
