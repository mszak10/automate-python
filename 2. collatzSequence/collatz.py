# Collatz Sequence from user input
def collatz(number):
    if number % 2 == 0:
        ret = number // 2
        print(ret)
        return ret
    else:
        ret = 3 * number + 1
        print(ret)
        return ret


print("Enter number:")
isInt = False
while not isInt:
    try:
        num = int(input())
        isInt = True
        while num != 1:
            num = collatz(num)
    except ValueError:
        print("Enter an integer!")
