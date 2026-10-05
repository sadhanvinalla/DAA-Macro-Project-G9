# Sum of Subsets using Backtracking

## Description

The Sum of Subsets problem finds a subset of a given set of numbers whose sum is equal to a specified target value.

For this project:

- Set = {5, 10, 12}
- Target Sum = 15

The problem is solved using the Backtracking technique. At each step, the algorithm makes two choices: include the current element or exclude it.

## Algorithm

1. Start with an empty subset and current sum 0.
2. Consider the elements one by one.
3. For each element, make two choices:
   - Include the element in the current subset.
   - Exclude the element from the current subset.
4. If the current sum becomes equal to the target sum, a solution is found.
5. If the current sum exceeds the target, stop exploring that branch.
6. Backtrack by removing the previously included element and explore the next possibility.
7. Continue until all possible choices have been explored.

For the given input:

```text
Set = {5, 10, 12}
Target = 15