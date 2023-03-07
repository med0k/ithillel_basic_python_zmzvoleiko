def group_by_surname(list_of_enrollees):
    group_counts = [0, 0, 0, 0]

    for enrollee in list_of_enrollees:
        surname = enrollee.split()[1]

        if ord('A') <= ord(surname[0]) <= ord('I'):
            group_counts[0] += 1
        elif ord('J') <= ord(surname[0]) <= ord('P'):
            group_counts[1] += 1
        elif ord('Q') <= ord(surname[0]) <= ord('T'):
            group_counts[2] += 1
        elif ord('U') <= ord(surname[0]) <= ord('Z'):
            group_counts[3] += 1

    return tuple(group_counts)


def main():
    enrollees = ['Maks Zvs', 'Michael Kosatik', 'Irina Bogdan', 'Iva Ivanich', 'William Shekspir']
    group_counts = group_by_surname(enrollees)
    print(group_counts)


if __name__ == "__main__":
    main()
