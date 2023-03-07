def lchain(*iterables):
    result = []
    for iterable in iterables:
        result.extend(iterable)
    return result


def main():
    list1 = [1, 2, 3]
    dict1 = {'a': 4, 'b': 5}
    tuple1 = (6, 7, 8)
    range1 = range(9, 12)

    result = lchain(list1, dict1, tuple1, range1)

    print(result)


if __name__ == "__main__":
    main()
