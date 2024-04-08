import json
import os

# get current working directory path
cwd_path = os.getcwd()


def linear_search(sek, num):
    pos = []
    vyskyt = 0
    slovnik = {'positions': 0,  'count':0}
    for i in range(len(sek)):
        if sek[i] == num:
            pos.append(i)
            vyskyt = vyskyt + 1
    slovnik["positions"] = pos
    slovnik["count"] = vyskyt

    return slovnik

def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    file_path = os.path.join(cwd_path, file_name)
    with open(file_name, "r") as file:
        data = json.load(file)
    return data[field]



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    print(linear_search(sequential_data, 8))
    pass


if __name__ == '__main__':
    main()