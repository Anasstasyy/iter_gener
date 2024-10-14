class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.coursor = 0
        self.internal_coursor = 0
        return self

    def __next__(self):
        if self.coursor == len(self.list_of_list)-1 and self.internal_coursor == len(self.list_of_list[-1]):
            raise StopIteration
        else:
            len_internal_list = len(self.list_of_list[self.coursor])
            if self.internal_coursor < len_internal_list:
                item = (self.list_of_list[self.coursor][self.internal_coursor])
                self.internal_coursor += 1
            else:
                self.coursor += 1
                self.internal_coursor = 0
                item = (self.list_of_list[self.coursor][self.internal_coursor])
                self.internal_coursor += 1
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
    FlatIterator(list_of_lists_1),
    ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
 test_1()