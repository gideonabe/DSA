# Item list: (name, weight, value)
items = [
    ("Water", 3, 10),
    ("Book", 1, 3),
    ("Food", 2, 9),
    ("Jacket", 2, 5),
    ("Camera", 1, 6)
]

capacity = 6
n = len(items)

# Create DP table: (n+1) x (capacity+1)
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

# Fill the table
for i in range(1, n + 1):
    name, wt, val = items[i - 1]
    for w in range(capacity + 1):
        if wt > w:
            dp[i][w] = dp[i - 1][w]
        else:
            dp[i][w] = max(dp[i - 1][w], val + dp[i - 1][w - wt])

# The maximum value
max_value = dp[n][capacity]
print("Maximum value:", max_value)

# Trace back to find which items were included
w = capacity
chosen_items = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:  # Item was included
        name, wt, val = items[i - 1]
        chosen_items.append(items[i - 1])
        w -= wt

# Print selected items
print("Items to take:")
for name, wt, val in reversed(chosen_items):
    print(f"- {name} (Weight: {wt}, Value: {val})")
