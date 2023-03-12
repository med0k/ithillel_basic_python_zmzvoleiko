"""
Написати функцію, що повертає усі прості числа від 1 до 100 у вигляді списку.
def gen_primes():  # returns list of ints
    pass
"""


def gen_primes() -> list:
    prime_numbers = []
    for numbers in range(2, 101):
        for i in prime_numbers:
            if not numbers % i:
                break
        else:
            prime_numbers.append(numbers)
    return prime_numbers


def main():
    print(f"Prime numbers from 1 to 100: {gen_primes()}")


if __name__ == "__main__":
    main()
