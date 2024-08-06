"""
Необязательное задание. Написать итератор, аналогичный итератору из задания 1,
но обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:
"""


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_reverse = list(reversed(list_of_list))

    def __iter__(self):
        return self

    def __next__(self):
        while self.list_reverse:
            element = self.list_reverse.pop()
            if isinstance(element, list):
                self.list_reverse.extend(reversed(element))
            else:
                return element
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()