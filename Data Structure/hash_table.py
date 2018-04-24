# TODO: code the basic hash algorithm
# TODO: finish the linked_list push method
# TODO: finish other basic colision method

import copy


class HashTable(object):
    def __init__(self, *args, **kwargs):
        length = kwargs.get('length')
        input_list = kwargs.get('input_list')
        method = kwargs.get('method')
        self.table = list(range(length))
        if input_list:
            if not method or method == 'linked':
                # this is the default method which is to create a linked list
                self._push_linked(input_list)
        else:
            pass

    def _push_linked(self, input_list):
        print(input_list)

    def _extend(self, size=None):
        if not size:
            self.table.extend(list(range(size)))


def main():
    # h_t = HashTable(length=10, input_list=list(range(10)))
    h_t = HashTable(length=10, input_list=None, method='linked')


if __name__ == '__main__':
    main()
