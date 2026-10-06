# 0/1 Knapsack Using Branch and Bound

## Project Overview

This project implements the 0/1 Knapsack Problem using the Branch and Bound technique in Python.

The main objective is to demonstrate how bounding and pruning can be used to efficiently find the maximum possible profit while satisfying the given knapsack capacity.

## Problem Statement

Given a set of items, where each item has a value and a weight, and a knapsack with a fixed capacity, select items such that:

* Each item is either selected or not selected.
* The total weight does not exceed the capacity of the knapsack.
* The total value is maximized.

## Example Input

```text
N = 5
W = 10

Values  = {40, 50, 100, 95, 30}
Weights = {2, 3.14, 1.98, 5, 3}
```

## Expected Output

```text
Maximum Profit = 235
Selected Items = {3, 1, 4}
Total Weight = 8.98
```

## Algorithm

The Branch and Bound algorithm explores possible solutions using a decision tree. For each item, there are two possible decisions:

1. Include the item.
2. Exclude the item.

Each node maintains the following information:

* Level: The current item being considered.
* Weight: The total weight of the selected items.
* Profit: The total value of the selected items.
* Bound: The maximum possible profit that can be obtained from the current node.

The items are sorted according to their value-to-weight ratio before calculating the bounds.

## Bounding

The upper bound of a node is calculated using the fractional knapsack approach.

The bound represents an optimistic estimate of the maximum profit that can be obtained from that node. It is used to determine whether a branch has the potential to produce a better solution.

## Pruning

A branch is pruned when it cannot produce a better solution.

There are two main pruning conditions:

### Weight-Based Pruning

If the total weight of a node exceeds the knapsack capacity, the branch is infeasible and is discarded.

```text
Current Weight > Capacity
```

### Bound-Based Pruning

If the upper bound of a node is less than or equal to the current best profit, there is no possibility of obtaining a better solution from that branch.

```text
Bound <= Current Best Profit
```

## Value-to-Weight Ratio

For the given example, the items are ordered according to their value-to-weight ratio.

| Item | Value | Weight | Value/Weight |
| ---- | ----: | -----: | -----------: |
| 3    |   100 |   1.98 |        50.51 |
| 1    |    40 |      2 |        20.00 |
| 4    |    95 |      5 |        19.00 |
| 2    |    50 |   3.14 |        15.92 |
| 5    |    30 |      3 |        10.00 |

## Optimal Solution

The optimal solution selects:

```text
Item 3
Item 1
Item 4
```

Total weight:

```text
1.98 + 2 + 5 = 8.98
```

Since:

```text
8.98 <= 10
```

the solution satisfies the capacity constraint.

Total profit:

```text
100 + 40 + 95 = 235
```

Therefore, the maximum profit is:

```text
235
```

## Files

```text
Project13_BranchAndBound.py
README.md
```

The main Python implementation is contained in:

```text
Project13_BranchAndBound.py
```

## Requirements

* Python 3.x
* Visual Studio Code
* Python extension for Visual Studio Code

No additional Python libraries are required.

## How to Run

Open the project folder in Visual Studio Code and open the terminal.

Run the following command:

```bash
python Project13_Knapsack.py
```

On Windows, if the `python` command is not recognized, use:

```bash
py Project13_Knapsack.py
```

## Expected Result

The program should produce a maximum profit of:

```text
Maximum Profit: 235
```

with the selected items:

```text
Selected Items: [3, 1, 4]
```

and total weight:

```text
Total Weight: 8.98
```

## Learning Objectives

This project demonstrates:

* The 0/1 Knapsack Problem
* Branch and Bound
* Upper-bound calculation
* Value-to-weight ratio
* Node evaluation
* Branch pruning
* Finding an optimal solution
* Implementation of the algorithm in Python
