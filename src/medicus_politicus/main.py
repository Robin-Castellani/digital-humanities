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

import pdfminer.high_level

from . import helpers


memoizer = helpers.Memoizer(cache_dir='./cache')


def cli():
    """Implement the Command Line Interface."""
    pass


@memoizer.memoize()
def read_file(filepath: pathlib.Path) -> str:
    """Read a .pdf file"""
    text = pdfminer.high_level.extract_text(filepath)
    return text

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
