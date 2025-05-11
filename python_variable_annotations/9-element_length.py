#!/usr/bin/env python3
"""
This module contains a type-annotated function 'element_length'
that works with iterable objects of sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence from the input and its length.

    Args:
        lst (Iterable[Sequence]): An iterable where each element is a sequence
                                  (e.g., a list of strings, a tuple of lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple
                                    contains a sequence and its integer length.
    """
    return [(i, len(i)) for i in lst]
