# x = [12, 33, 55, 67, 7, 88]

'''for item in x:
    print(item)

'''
'''for item in enumerate(x):
    print(type(x), item)
'''

'''for item in range(0, 10, 2):
    print(item)


'''


'''count = 0
while count < 10:
    print("count", count)
    count += 1'''

'''count = 0
while True:
    if count == 10:
        break

    print("Count", count)
    count += 2'''


'''count = 0
while True:
    if count == 10:
        break

    print("Count", count)
    count += 3'''

x = range(10)
for i in x:
    if i % 2 == 0:
        continue
    print('Hi')
