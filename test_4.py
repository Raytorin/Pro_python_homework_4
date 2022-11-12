import types


def flat_generator(list_of_list):
    temp = []
    example = []
    temp_elder_list = list_of_list.copy()
    while True:
        check_count = 0
        for main_loop in temp_elder_list:
            if type(main_loop) == type(example):
                temp.extend(main_loop)
            else:
                temp.append(main_loop)
        for check_loop in temp:
            if type(check_loop) != type(example):
                check_count += 1
            else:
                break
        if check_count == len(temp):
            final_list = temp.copy()
            break
        temp_elder_list = temp.copy()
        temp.clear()
    for list_item in final_list:
        yield list_item


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
