"""Collection of useful functions."""

import pathlib
from typing import List, Tuple

import pdfminer.high_level
from . import helpers

memoizer = helpers.Memoizer(cache_dir='./cache')


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