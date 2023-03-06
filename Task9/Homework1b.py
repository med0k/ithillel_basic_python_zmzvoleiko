import random


def diff_min_max(numero_limitaro, minimum_number, maximum_number):
    numbers = [random.randint(minimum_number, maximum_number) for _ in range(numero_limitaro)]
    min_numb = numbers[0]
    max_numb = numbers[0]
    for i in numbers:
        if i < min_numb:
            min_numb = i
        elif i > max_numb:
            max_numb = i
    return max_numb - min_numb


def main():
    numero_limitaro = int(input('Enter num limit: '))
    minimum_number = int(input('Enter lower bound: '))
    maximum_number = int(input('Enter upper bound: '))

    difference = diff_min_max(numero_limitaro, minimum_number, maximum_number)

    print(f"Difference between minimum number and maximum number is: {difference}")


if __name__ == "__main__":
    main()
