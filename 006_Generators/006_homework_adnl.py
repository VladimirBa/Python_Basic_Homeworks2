def find_prime():
    num = 2
    prime_index = 20
    while count <= prime_index:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            yield num
        num += 1


count = 1
for element in find_prime():
    count += 1
    print(element, end=' ')
