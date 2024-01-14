numbers = [0, 3, 8, -4, 9, 1]

def isEven(number):
    if number % 2 == 0:
        print(f'This number, {number} is even')
        return True
    else:
        print(f'This number, {number} is odd')
        return False

list(filter(isEven, numbers))

print(list)