# Define the items with their weights and profits
items = ["Gold", "Silver", "Copper", "Vase", "Mirror"]
weights = [1, 2, 5, 6, 7]
profits = [1, 6, 18, 22, 28]
capacity = 11

# Number of items
n = len(items)

# Create a DP table with dimensions (n+1) x (capacity+1)
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Build the DP table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(dp[i - 1][w], profits[i - 1] + dp[i - 1][w - weights[i - 1]])
        else:
            dp[i][w] = dp[i - 1][w]

# Backtrack to find which items are included
w = capacity
selected_items = []
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(items[i - 1])
        w -= weights[i - 1]

# Display the results
print("Maximum Profit:", dp[n][capacity])
print("Selected Items:", selected_items)

# Display the DP table
print("\nDP Table:")
for row in dp:
    print(row)
