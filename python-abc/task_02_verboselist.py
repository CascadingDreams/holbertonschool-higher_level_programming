#!/usr/bin/env python3

'''VerboseList module - extends built in list'''


class VerboseList(list):
    '''
    Creates VerboseList class.

    A list that prints notification messages when items are added or removed.

    Extends the built-in list class and overrides modification methods to
    provide verbose feedback about list operations.
    '''
    def append(self, item):
        '''
        Adds item to end of list.
        Prints notif
        Args:
            item: item to add to list.
        '''
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        '''
        Extends list with x items.
        Prints notif
        Args:
            x: num of items added
        '''
        items_list = list(items)
        super().extend(items_list)
        print(f"Extended the list with [{len(items_list)}] items.")

    def remove(self, item):
        '''
        Prints notif
        Removes item from list
        Args:
            item: item to remove
        '''
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        '''
        Prints notif
        Pops item from list
        Args:
            index: index of item to pop (default: -1)
        '''
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
