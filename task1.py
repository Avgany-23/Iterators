"""
Доработать класс FlatIterator в коде ниже. Должен получиться итератор,
который принимает список списков и возвращает их плоское представление, 
т. е. последовательность, состоящую из вложенных элементов. 
Функция test в коде ниже также должна отработать без ошибок.
"""

from copy import deepcopy


# --- Первый способ ---
class FlatIterator1:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.stop_iter = len(list_of_list)

    def __iter__(self):
        self.index_general = 0
        self.index_inside = 0
        return self

    def __next__(self):
        if self.index_general < self.stop_iter:
            self.index_inside += 1
            self.index_inside_copy = self.index_inside - 1

            if self.index_inside == len(self.list_of_list[self.index_general]):
                self.index_inside = 0
                self.index_general += 1
                return self.list_of_list[self.index_general - 1][self.index_inside_copy]

            return self.list_of_list[self.index_general][self.index_inside - 1]

        else:
            raise StopIteration


# --- Первый способ ---
class FlatIterator2:

    def __init__(self, list_of_list):
        self.list_of_list = deepcopy(list_of_list)
        self.len_list = len(list_of_list)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        if self.list_of_list:
            if len(self.list_of_list[0]) == 1:
                result_element = self.list_of_list[0].pop(0)
                self.list_of_list.pop(0)
                self.index = 0
                return result_element

            return self.list_of_list[0].pop(0)
        else:
            raise StopIteration


def test_1():

    list_of_lists_1 = [['a', 'b', 'c'],
                       ['d', 'e', 'f', 'h', False],
                       [1, 2, None]]

    for flat_iterator_item, check_item in zip(FlatIterator1(list_of_lists_1),
                                              ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):

        assert flat_iterator_item == check_item

    assert list(FlatIterator1(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def test_2():

    list_of_lists_1 = [['a', 'b', 'c'],
                       ['d', 'e', 'f', 'h', False],
                       [1, 2, None]]

    for flat_iterator_item, check_item in zip(FlatIterator2(list_of_lists_1),
                                              ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):

        assert flat_iterator_item == check_item

    assert list(FlatIterator2(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    test_2()