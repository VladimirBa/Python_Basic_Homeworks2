class ReversedList:

    def __init__(self, my_list):

        self.my_list = my_list
        self.index = len(my_list) - 1

    def __iter__(self):

        return self

    def __next__(self):

        if self.index < 0:
            raise StopIteration

        next_elem = self.my_list[self.index]
        self.index -= 1

        return next_elem


def main():
    my_list = ['a', 1, 'z', -9, 'A', 10]
    list_print = []
    for i in ReversedList(my_list):
        list_print.append(str(i))
    print(*list_print, sep=', ')


if __name__ == '__main__':
    main()
