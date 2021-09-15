my_list = [2, 5, 1, 23, -7, 11, 0, 8, 12]


def num_gen():

    res = [x ** 2 for x in my_list if x % 2 == 0]
    print(res)


def num_cycle():
    res_list = []
    for x in my_list:
        if x % 2 == 0:
            y = x ** 2
            res_list.append(y)
        else:
            continue
    print(res_list)


if __name__ == '__main__':
    num_gen()
    num_cycle()
