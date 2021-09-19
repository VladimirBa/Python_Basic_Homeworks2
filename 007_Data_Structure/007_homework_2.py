a = '1_2,40_5,5_32'
c = [int(num.split('_')[0]) + int(num.split('_')[1]) for num in a.split(',')]
print(c)
