d = {
    'a': {'1': [1, 2, 3, 4],
          '2': ['w', 'x', 'y', 'z']},
    'b': {'name': ['Sam', 'John'],
          'surname': ['Doe', 'Smith']}
}
new_d = []


def func():
    for key1, val1 in d.items():
        for key2, val2 in val1.items():
            for element in val2:
                new_d.append(element)
    return new_d


print(func())
