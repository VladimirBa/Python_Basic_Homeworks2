def func(index, count):
    return {
        "ID": index,
        "values": [f"{index}_{value}" for value in range(count)]
    }


def get_index(count):
    return [func(i, j) for i, j in zip(range(count), list(range(count))[::-1])]


count = 5
sublists = get_index(count)

flattened = [element for sublist in sublists for element in sublist['values']]
print(flattened)
