
# 0/1 Knapsack using Dynamic Programming

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]

capacity = 10
n = len(weights)

# Create DP table
dp = [[0 for _ in range(capacity + 1)]
      for _ in range(n + 1)]

# Fill the DP table
for i in range(1, n + 1):
    for w in range(capacity + 1):

        if weights[i - 1] <= w:
            include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
            exclude = dp[i - 1][w]
            dp[i][w] = max(include, exclude)

        else:
            dp[i][w] = dp[i - 1][w]

# Display the DP table
print("DP Table:")
print("Items/Capacity", *range(capacity + 1))

for i in range(n + 1):
    print(i, *dp[i])

print("\nMaximum value:", dp[n][capacity])

# Find selected items
w = capacity
selected = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected.append(i)
        w -= weights[i - 1]

print("Selected items:", selected[::-1])