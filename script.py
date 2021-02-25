# Code for creating iterator


list = [1, 2, 3, 4, 5]
iterator = iter(list)
print(next(iterator))
print(next(iterator))


# Code for creating generator


def fibonacci():
    a, b = [1, 1]
    for i in range(10):
        yield b
        b += a
        a, b = b, a


for number in fibonacci():
    print(number)


# code for creating decorator


def cat(func):
    print("Cat's name is: ")
    func()


@cat
def name():
    print("Vasya")
    pass


# Code for creating context manager


with open('text.txt', 'r') as file:
    for line in file:
        print(line)
