"""
1.2 Smallest Subarray with a Given Sum

Given an array of positive numbers and a positive number ‘S,’
find the length of the smallest contiguous subarray whose sum
is greater than or equal to ‘S’. Return 0 if no such subarray
exists.
"""

def smallest_sum_subarray(arr, k):
    first_index = 0
    last_index = 0
    lowest_sum = 0
    summation = 0
    sub_arr_size = sum(arr)

    for i in arr:
        summation = summation + i

        if (summation >= k):
            if last_index - first_index < sub_arr_size:
                sub_arr_size = last_index - first_index
            summation = summation - arr[first_index]
            first_index = first_index + 1

        last_index = last_index + 1
    print(sub_arr_size)

def main():
    first_list = [2, 1, 5, 2, 3, 2]
    target = 7

    second_list = [2, 1, 5, 2, 8]
    second_target = 7

    smallest_sum_subarray(first_list, target)
    smallest_sum_subarray(second_list, target)

if __name__ == "__main__":
    main()
