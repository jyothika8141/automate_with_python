def collatz(number):
    if number == 1:
        return None
    elif number % 2 == 0:
        new_num = number // 2
    else:
        new_num = 3 * number + 1
    print(new_num)
    collatz(new_num)


try:
    num = int(input("Enter a number: "))
    collatz(num)
except ValueError:
    print("should enter an integer")
