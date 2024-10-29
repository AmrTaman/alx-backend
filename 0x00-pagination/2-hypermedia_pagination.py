#!/usr/bin/env python3
"""
this is module
"""
import csv
import math
from typing import List, Tuple, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        this is method
        """
        return ((page - 1) * page_size, page * page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        iam here
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        pag_range = self.index_range(page, page_size)
        dataset = self.dataset()
        if pag_range[1] > len(dataset):
            return []
        return dataset[pag_range[0]: pag_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        we are here
        """
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        total = math.ceil(len(dataset) / page_size)
        prev_p = None if page == 1 else page - 1
        next_p = None if page > total else page + 1
        return {
                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_p,
                'prev_page': prev_p,
                'total_pages': total
                }
