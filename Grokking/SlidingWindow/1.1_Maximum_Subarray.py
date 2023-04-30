
"""
Find the Max Sum Subarray
"""
def MaxSumSub(list, k):
    first_index = 0
    last_index = 0
    summation = 0
    current_max = 0

    for i in list:
        summation = summation + i

        if last_index - first_index == k - 1:
            if summation > current_max:
                current_max = summation
            summation = summation - list[first_index]
            first_index = first_index + 1

        last_index = last_index + 1
    print("Max sub: ", current_max)


def main():
    first_list = [2, 1, 5, 1, 3, 2]
    first_size = 3

    second_list = [2, 3, 4, 1, 5]
    second_size = 2

    MaxSumSub(first_list, first_size)
    MaxSumSub(second_list, second_size)


if __name__ == "__main__":
    main()
