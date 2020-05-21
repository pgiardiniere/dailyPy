# print numbers from 1 to n.

# If num is divisible by 3, print 'Fizz'
# if num is divisible by 5, print 'Buzz'
# if num is divisible by both, print FizzBuzz


def fizz_buzz(N):
    for i in range(1, N+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    fizz_buzz(16)
