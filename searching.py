import os

# get current working directory path
cwd_path = os.getcwd()


# def linear_search(sek, num):
#
#     for i in range(len(sek)):
#         if sek[i] == num:



def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    file_path = os.path.join(cwd_path, file_name)
    with open(file_name, "r") as file:
        



def main():
    pass


if __name__ == '__main__':
    main()