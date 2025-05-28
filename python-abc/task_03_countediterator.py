#!/usr/bin/env python3

'''Module for CountedIterator class to modify __next__'''


class CountedIterator:
    '''Creates CountedIterator class'''

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.

        Args:
            iterable: Any iterable object (list, tuple, string, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the counter.
        Returns:
            The next item from the underlying iterator
        Raises:
            StopIteration: When there are no more items to iterate
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Get the current count of items that have been iterated.
        Returns:
            int: The number of items that have been fetched so far
        """
        return self.count
