def get_reversed_list():
    my_list = ['a', 1, 'z', -9, 'A', 10]
    my_rev_list = [elem for elem in my_list[::-1]]
    yield my_rev_list


gen = get_reversed_list()
print(next(gen))
