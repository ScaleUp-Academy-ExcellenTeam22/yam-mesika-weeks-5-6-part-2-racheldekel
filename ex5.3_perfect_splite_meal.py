def perfect_split():
    """
    generator that check if the number is perfect split
    :return:
    """
    current_number = 0
    while True:
        if is_perfect(current_number):
            yield current_number
        current_number = current_number + 1


def is_perfect(n):
    """ If sum of divisors is equal to
    # n, then n is a perfect number
    """
    sum_num = 1

    i = 2
    while i * i <= n:
        if n % i == 0:
            sum_num = sum_num + i + n / i
        i += 1

    return True if sum_num == n and n != 1 else False


if __name__ == '__main__':
    our_generator = perfect_split()
    print("Below are all perfect numbers till 10000")
    for number in our_generator:
        print(number, " is a perfect number")
