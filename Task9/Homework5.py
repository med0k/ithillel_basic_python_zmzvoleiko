def group_by_surname(list_of_enrollees):
    group_counts = [0, 0, 0, 0]

    for enrollee in list_of_enrollees:
        surname = enrollee.split()

        if len(surname) == 0:
            continue

        first_letter = surname[0].upper()

        if 'A' <= first_letter <= 'I':
            group_counts[0] += 1
        elif 'J' <= first_letter <= 'P':
            group_counts[1] += 1
        elif 'Q' <= first_letter <= 'T':
            group_counts[2] += 1
        elif 'U' <= first_letter <= 'Z':
            group_counts[3] += 1

    return tuple(group_counts)


def main():
    enrollees = ['Maks Zvs', 'Michael Kosatik', 'Irina Bogdan', 'Iva Ivanich', 'William Shekspir']
    group_counts = group_by_surname(enrollees)
    print("Group A-I: {}".format(group_counts[0]))
    print("Group J-P: {}".format(group_counts[1]))
    print("Group Q-T: {}".format(group_counts[2]))
    print("Group U-Z: {}".format(group_counts[3]))


if __name__ == "__main__":
    main()
