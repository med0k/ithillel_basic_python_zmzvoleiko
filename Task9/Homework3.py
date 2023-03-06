def copydeep(obj):
    if isinstance(obj, (int, float, str, bool)):
        return obj
    elif isinstance(obj, list):
        new_list = []
        for elem in obj:
            new_list.append(copydeep(elem))
        return new_list
    elif isinstance(obj, tuple):
        new_tuple = ()
        for elem in obj:
            new_tuple += (copydeep(elem))
        return new_tuple
    elif isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            new_dict[key] = copydeep(value)
        return new_dict
    else:
        return None


def main():
    d = {'a': 1, 'b': [2, 3]}
    d_copy = copydeep(d)
    d['b'].append(4)
    print(d, d_copy)


if __name__ == "__main__":
    main()
