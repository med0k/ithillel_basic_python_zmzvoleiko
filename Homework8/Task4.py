"""
Написати функцію, що повертає усі прості числа від 1 до 100 у вигляді списку.
def gen_primes():  # returns list of ints
    pass
"""


def my_numbers():
    numbers = []
    for i in range(1, 101):
        is_numbers = True
        for measure in range(2, int(i ** 0.5) + 1):
            if i % measure == 0:
                is_numbers = False
                break
        if is_numbers:
            numbers.append(i)
    return numbers


def main():
    print(my_numbers())


if __name__ == "__main__":
    main()
