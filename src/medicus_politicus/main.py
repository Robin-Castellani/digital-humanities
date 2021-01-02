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

import pdfminer.high_level

from . import helpers


memoizer = helpers.Memoizer(cache_dir='./cache')


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


"""
@click.command()
@click.option("--file", help="file originale")
@click.option("--file-sostituzioni", help="File con le sostituzioni da effettuare")
@click.option("--output-name", help="Nome del file risultante.")
def sostituisci(file, file_sostituzioni, output_name):
    f = leggi_file(file)
    f_sostituito = effettua_sostituzioni(f, file_sostituzioni)
    scrivi_file(f_sostituito, name=output_name)
"""

if __name__ == '__main__':
    cli()
