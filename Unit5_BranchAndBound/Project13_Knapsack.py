# 0/1 Knapsack using Branch and Bound
# Example:
# N = 5, W = 10
# Values  = {40, 50, 100, 95, 30}
# Weights = {2, 3.14, 1.98, 5, 3}

class Item:
    def __init__(self, value, weight, index):
        self.value = value
        self.weight = weight
        self.index = index
        self.ratio = value / weight


class Node:
    def __init__(self, level, weight, profit, bound, path):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.path = path


# Calculate upper bound using fractional knapsack
def calculate_bound(node, capacity, items):

    if node.weight >= capacity:
        return 0

    bound = node.profit
    total_weight = node.weight
    i = node.level

    while i < len(items) and total_weight + items[i].weight <= capacity:
        total_weight += items[i].weight
        bound += items[i].value
        i += 1

    # Add fraction of next item
    if i < len(items):
        remaining = capacity - total_weight
        bound += remaining * items[i].ratio

    return bound


# Branch and Bound
def knapsack_branch_and_bound(values, weights, capacity):

    items = [
        Item(values[i], weights[i], i + 1)
        for i in range(len(values))
    ]

    # Sort by value/weight ratio
    items.sort(key=lambda x: x.ratio, reverse=True)

    print("\nItems sorted by Value/Weight ratio:")
    print("-" * 55)

    for item in items:
        print(
            f"Item {item.index}: "
            f"Weight={item.weight}, "
            f"Value={item.value}, "
            f"Ratio={item.ratio:.2f}"
        )

    root = Node(0, 0, 0, 0, [])

    root.bound = calculate_bound(root, capacity, items)

    queue = [root]

    max_profit = 0
    best_path = []

    print("\n\nBRANCH AND BOUND TREE")
    print("=" * 70)

    while queue:

        node = queue.pop(0)

        # Prune if bound cannot beat current best
        if node.bound <= max_profit:
            print(
                f"PRUNED -> Level={node.level}, "
                f"Weight={node.weight:.2f}, "
                f"Profit={node.profit:.2f}, "
                f"Bound={node.bound:.2f}"
            )
            continue

        # If all items have been considered
        if node.level == len(items):
            continue

        item = items[node.level]

        # -------------------------------------------------
        # INCLUDE ITEM
        # -------------------------------------------------

        include_weight = node.weight + item.weight
        include_profit = node.profit + item.value

        include_path = node.path + [item.index]

        if include_weight <= capacity:

            include_node = Node(
                node.level + 1,
                include_weight,
                include_profit,
                0,
                include_path
            )

            include_node.bound = calculate_bound(
                include_node,
                capacity,
                items
            )

            print(
                f"INCLUDE Item {item.index} -> "
                f"Weight={include_node.weight:.2f}, "
                f"Profit={include_node.profit:.2f}, "
                f"Bound={include_node.bound:.2f}"
            )

            if include_profit > max_profit:
                max_profit = include_profit
                best_path = include_path

            if include_node.bound > max_profit:
                queue.append(include_node)
            else:
                print("    --> PRUNED (Bound <= Best Profit)")

        else:
            print(
                f"INCLUDE Item {item.index} -> "
                f"Weight={include_weight:.2f} "
                f"> {capacity} --> PRUNED"
            )

        # -------------------------------------------------
        # EXCLUDE ITEM
        # -------------------------------------------------

        exclude_node = Node(
            node.level + 1,
            node.weight,
            node.profit,
            0,
            node.path
        )

        exclude_node.bound = calculate_bound(
            exclude_node,
            capacity,
            items
        )

        print(
            f"EXCLUDE Item {item.index} -> "
            f"Weight={exclude_node.weight:.2f}, "
            f"Profit={exclude_node.profit:.2f}, "
            f"Bound={exclude_node.bound:.2f}"
        )

        if exclude_node.bound > max_profit:
            queue.append(exclude_node)
        else:
            print("    --> PRUNED (Bound <= Best Profit)")

    print("\n" + "=" * 70)
    print("FINAL RESULT")
    print("=" * 70)

    print("Maximum Profit:", max_profit)
    print("Selected Items:", best_path)

    total_weight = sum(
        weights[i - 1] for i in best_path
    )

    print("Total Weight:", total_weight)


# ---------------------------------------------------------
# INPUT
# ---------------------------------------------------------

values = [40, 50, 100, 95, 30]
weights = [2, 3.14, 1.98, 5, 3]
capacity = 10

knapsack_branch_and_bound(
    values,
    weights,
    capacity
)