import random


def diff_nech_chet(numero_limitaro, minimum_number, maximum_number):
    chetn_sum = 0
    nechetn_sum = 0

    for i in range(numero_limitaro):
        numb = random.randint(minimum_number, maximum_number)
        if numb % 2 == 0:
            chetn_sum += numb
        else:
            nechetn_sum += numb

    return chetn_sum - nechetn_sum


def main():
    numero_limitaro = int(input('Enter num limit: '))
    minimum_number = int(input('Enter lower bound: '))
    maximum_number = int(input('Enter upper bound: '))

    difference = diff_nech_chet(numero_limitaro, minimum_number, maximum_number)

    print(f"Difference between chetnie numbers and nechetnie numbers is: {difference}")


if __name__ == "__main__":
    main()
