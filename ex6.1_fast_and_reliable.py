import time
from typing import IO


def amount_list_time(file: IO[str]):
    """
    function that receive file and read all the words in it, and calculate average time take
    :param file:
    """
    words_list = [], set
    data = file.read()
    words_list = data.split()
    return ("search in list take " + average_runtime(words_list).__str__())

def amount_set_time(file: IO[str]):
    """
    function that receive file and read all the words in it, and calculate average time take
    :param file:
    """
    words_set = [], set
    data = file.read()
    words_set = set(words_list)
    return ("search in set take " + average_runtime(words_set).__str__())

def average_runtime(list_or_set: list / set) -> float:
    """
    function that check the average time take to find the word zwitterion
    :param
    :return:
    """
    sum_time = 0
    for check_number in range(1000):
        start = time.time()
        end = time.time()
        sum_time += end - start
    return sum_time / 1000


if __name__ == '__main__':
    words_list = amount_list_time("words.txt")
    words_set = amount_set_time("words.txt")

    amount_of_list_time = average_runtime(words_list)
    amount_of_set_time = average_runtime(words_set)

    print("search in list take " + amount_of_list_time)
    print("search in set take " + amount_of_set_time)
