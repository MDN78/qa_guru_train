
olo = ['any', 1, 2, [3, 4, 5], 'two']
print(olo[3][1])

# take with space

lst = [ 1, 3, 4, 5, 1, 2, 3, 5, 1, 6]
lst.append('new')
print(lst)
print(lst.count(1))

lst = []
for i in range(1, 11):
    lst.append(i)
print(lst)
lst.append(14)
print(lst)

lst.sort(reverse=True)
print(lst)
lst.pop(0) # remove by index
print(lst)
lst.remove(8) # remove by item
print(lst)

'''
Выведите всю матрицу в одном выражении.
Выведите по отдельности каждую строку матрицы.
Выведите по отдельности каждый элемент матрицы.
Вывести с помощью цикла в красивом виде print(element, end=' ')
'''

matrix = [
[11, 12, 13],
[21, 22, 23],
[31, 32, 33]
]

print(matrix[0])
print(matrix[1])
print(matrix[2])


for i in matrix:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')

sp = [ 1, 3, 4, 5, 1, 2, 3, 5, 1, 6, 1, 3]
sp1 = []
for element in sp:
    if element not in sp1:
        sp1.append(element)
sp1.sort()
print(sp1)