from typing import Iterator


def inteleave(*args) -> Iterator[any]:
    """
    function that get args as parameter and zip the lists
    :param args:
    :return:
    """
    for elem in zip(*args):
        for item in elem:
            yield item


if __name__ == '__main__':
    for item in inteleave('abc', [1, 2, 3], ('!', '@', '#')):
        print(item)
