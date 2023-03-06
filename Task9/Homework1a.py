import random


def diff_min_max(numero_limitaro, minimum_number, maximum_number):
    numbers = [random.randint(minimum_number, maximum_number) for _ in range(numero_limitaro)]
    return max(numbers) - min(numbers)


def main():
    numero_limitaro = int(input('Enter num limit: '))
    minimum_number = int(input('Enter lower bound: '))
    maximum_number = int(input('Enter upper bound: '))

    difference = diff_min_max(numero_limitaro, minimum_number, maximum_number)

    print(f"Difference between lower bound and upper bound is: {difference}")


if __name__ == "__main__":
    main()
