# 0/1 Knapsack Using Dynamic Programming

## Description

This project solves the 0/1 Knapsack problem using Dynamic Programming. The goal is to maximize the total value of selected items without exceeding the capacity of the bag.

## Input

* Weights: [2, 3, 4, 5]
* Values: [3, 4, 5, 6]
* Capacity: 10

## Algorithm

1. Create a DP table with n+1 rows and W+1 columns.
2. Initialize the table with zeros.
3. For every item and capacity, check whether the item fits.
4. If it fits, choose the maximum of including or excluding the item.
5. Otherwise, copy the value from the previous row.
6. The final answer is stored in DP[n][W].

## Complexity

* Time Complexity: O(nW)
* Space Complexity: O(nW)

## Prompt Used

Create a DP table for 0/1 Knapsack with 4 items and capacity 10, highlighting the maximum value and selected items.

## Output

Maximum value: 13
Selected items: [1, 2, 4]

## Learning Outcomes

* Understood the 0/1 Knapsack problem.
* Learned how Dynamic Programming uses a table.
* Understood time and space complexity.
* Practiced AI-based visualization and GitHub documentation.
