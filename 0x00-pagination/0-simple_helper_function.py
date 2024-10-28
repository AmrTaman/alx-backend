#!/usr/bin/env python3
"""
this is an offset and indexing function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    this is method
    """
    return ((page - 1) * page_size, page * page_size)
