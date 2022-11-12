class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor = -1
        self.temp = []
        return self

    def __next__(self):
        if len(self.temp) == 0:
            temp_list = []
            example = []
            temp_elder_list = self.list_of_list.copy()
            check_while = 0
            while check_while != 1:
                check_count = 0
                for main_loop in temp_elder_list:
                    if type(main_loop) == type(example):
                        temp_list.extend(main_loop)
                    else:
                        temp_list.append(main_loop)
                for check_loop in temp_list:
                    if type(check_loop) != type(example):
                        check_count += 1
                    else:
                        break
                if check_count == len(temp_list):
                    self.temp = temp_list.copy()
                    check_while = 1

                temp_elder_list = temp_list.copy()
                temp_list.clear()
        self.cursor += 1
        if self.cursor == len(self.temp):
            raise StopIteration
        return self.temp[self.cursor]


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
