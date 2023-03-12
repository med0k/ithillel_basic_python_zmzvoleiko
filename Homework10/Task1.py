from typing import Union


def copydeep(obj: Union[str, int, float, bool, list, dict], memory=None) -> Union[str, int, float, bool, list, dict]:
    if memory is None:
        memory = {}

    obj_id = id(obj)
    if obj_id in memory:
        return memory[obj_id]

    if isinstance(obj, (int, float, str, bool)):
        return obj
    elif isinstance(obj, list):
        copy_list = []
        memory[obj_id] = copy_list
        for item in obj:
            copy_list.append(copydeep(item, memory))
        return copy_list
    elif isinstance(obj, dict):
        copy_dict = {}
        memory[obj_id] = copy_dict
        for key, value in obj.items():
            copy_dict[copydeep(key, memory)] = copydeep(value, memory)
        return copy_dict


def main():
    test_data = [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658]}, 2.0, {'e': 0}]
    test_data[3]['d'] = test_data
    test_data[-1]['f'] = test_data[-1]
    copy = copydeep(test_data)
    print(test_data)
    print(copy)
    print(copy[3]['c'] is not test_data[3]['c'])  # True
    print(copy[3]['d'] is not test_data[3]['d'])  # True
    print(copy[3]['d'] is copy)  # True
    print(copy[-1] is not test_data[-1])  # True
    print(copy[-1] is copy[-1]['f'])  # True


if __name__ == "__main__":
    main()
