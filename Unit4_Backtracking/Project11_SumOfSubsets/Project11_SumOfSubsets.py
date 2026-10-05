# Sum of Subsets using Backtracking

numbers = [5, 10, 12]
target = 15


def sum_of_subsets(index, current_sum, subset):

    # If the target sum is reached
    if current_sum == target:
        print("Solution found:", subset)
        return

    # Stop if we have checked all numbers
    if index == len(numbers):
        return

    # Stop if current sum exceeds the target
    if current_sum > target:
        return

    # Choice 1: Include the current number
    subset.append(numbers[index])

    sum_of_subsets(
        index + 1,
        current_sum + numbers[index],
        subset
    )

    # Backtrack: remove the number
    subset.pop()

    # Choice 2: Exclude the current number
    sum_of_subsets(
        index + 1,
        current_sum,
        subset
    )


# Start the backtracking process
sum_of_subsets(0, 0, [])