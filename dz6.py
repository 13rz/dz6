# #ЧАСТИНА 1
# def home1():
#     my_string = "0123456789"
#     for i in my_string:
#         for j in my_string:
#             print(int(i+j), end=" ")
# home1()

#ЧАСТИНА 2
#A
n = int(input("n="))
for i in range(n):
    for j in range(i,n):
        print(' ', end = ' ')
    for j in range (i):
        print('*', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()
#B
n = int(input("n="))
for i in range(n):
    for j in range(n - i):
        print(' ', end ='')
    for j in range(2 * i + 1):
        if j == 0:
            print('*', end='')
        elif j ==2 * i:
            print('*', end='')
        elif i == n - 1:
            print('*', end='')
        else:
            print(' ', end='')

    print()

#C
N = int(input("n="))
for i in range(1, N + 1):
    for j in range(1, N - i + 1):
        print(end = ' ')
    for l in range(1, 2 * i):
        if l == 1 or l == i * 2 - 1:
            print('*', end = '')
        else:
            print('*', end = '')
    print()
for i in range(N - 1, 0, -1):
    for j in range(1, N - i + 1):
        print(' ', end = '')
    for l in range(1, 2 * i):
        if l == 1 or l == i * 2 - 1:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
#D
n = int(input("n="))
for i in range(n):
    for j in range(i,n):
        print(' ', end = ' ')
    for j in range (i):
        print('*', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()
for i in reversed(range(n - 2)):
        print(int((n - i - 1)) * '  ', '* ', int((i * 2 + 1) / 2) * '  ', '*',
              int((i * 2 + 1) / 2) * '  ', ' *', sep='')
print(n * '  ', '*', sep='')

