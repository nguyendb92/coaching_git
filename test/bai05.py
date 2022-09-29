def divisible(a):
    for i in range(a[0], a[-1] + 1):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')


m = [int(n) for n in input().split()]
print(divisible(m))
