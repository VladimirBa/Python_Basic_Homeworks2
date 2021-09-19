d = {
    'a': {'1': [1, 2, 3, 4],
          '2': ['w', 'x', 'y', 'z']},
    'b': {'name': ['Sam', 'John'],
          'surname': ['Doe', 'Smith']}
}
new_d = []
for key1, val1 in d.items():
    for key2, val2 in val1.items():
        for i in val2:
            new_d.append(i)
print(new_d)
