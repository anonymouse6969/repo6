
def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= weights[i - 1]

    return dp[n][capacity], selected[::-1], dp

n = int(input("Enter number of items: "))
weights = []
values = []

for i in range(n):
    print("Item", i + 1)
    weights.append(int(input("Enter weight: ")))
    values.append(int(input("Enter value: ")))

capacity = int(input("Enter knapsack capacity: "))

if n <= 0 or capacity < 0 or any(w <= 0 for w in weights) or any(v < 0 for v in values):
    print("Enter valid weights, values and capacity.")
else:
    maximum, selected, table = knapsack(weights, values, capacity)

    print("\nDP Table:")
    for row in table:
        print(row)

    print("\nMaximum value:", maximum)
    print("Selected items:", selected)
