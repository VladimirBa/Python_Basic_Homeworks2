def iter_elements():
    my_list = ['a', 1, 'z', -9, 'A', 10]
    iter_object = iter(my_list)
    while True:
        try:
            list_elem = next(iter_object)
            print(list_elem)
        except StopIteration:
            break


if __name__ == '__main__':
    iter_elements()
