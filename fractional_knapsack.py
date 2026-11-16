
def fractional_knapsack(weights, values, capacity):
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    items.sort(reverse=True)

    total_value = 0

    for ratio, weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            capacity = 0

    return total_value

n = int(input("Enter number of items: "))
weights = []
values = []

for i in range(n):
    print("Item", i + 1)
    weights.append(float(input("Enter weight: ")))
    values.append(float(input("Enter value: ")))

capacity = float(input("Enter knapsack capacity: "))

if n <= 0 or capacity < 0 or any(w <= 0 for w in weights) or any(v < 0 for v in values):
    print("Enter valid weights, values and capacity.")
else:
    maximum_value = fractional_knapsack(weights, values, capacity)
    print("Maximum value:", round(maximum_value, 2))
