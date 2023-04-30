
list = [1, 3, 2, 6, -1, 4, 1, 8, 2]
result = []
size = 5

"""
Solution 2 (Optimized)

Instead of needing to reiterating through the list by sublist
and calculation the average for each sublist.

Instead, we can keep the calculation from the previous sum minus
the first item from the previous sublist plus the the new, added
item from the new sublist. Thus only needing one for-loop
"""

# Need to keep track of starting index and ending index
def main():
    first_index = 0
    last_index = 0
    moving_sum = 0

    for i in list:

        # Add item to moving_sum each iteration
        moving_sum = moving_sum + i

        if (last_index - first_index == size - 1):
            result.append(moving_sum/5)
            moving_sum = moving_sum - list[first_index]
            first_index = first_index + 1

        last_index = last_index + 1
    print("This is the last index: ", last_index)
    print("Result list:", result)

"""
Solution 1

This first solution goes through the list several times
take average of a window, but it's suboptimal at the point
to regroup the list by groups of 5 and taking the average
for each subgroup. This would take n * n-m otherwise
written as O(n^2)

Calculation of Big O Notation was incorrect. The actual
Big O Notation is O(N*K).

N - the number of elements in the array
M - sum of it's next 'K' elements

AH! This is the number of iterations of the outer loop
multiplied by the number of iterations of the inner loop.
"""

"""
# Iterates through the list minus last 5 items
for i in range(len(list)-4):
  summation = 0
  for j in range(i, i+5):
    # Iterates through the sub list
    summation = summation + list[j]
  result.append(summation/5)

print("This is the result: ", result)
"""

if __name__ == "__main__":
    main()
