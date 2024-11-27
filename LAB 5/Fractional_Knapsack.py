import random

class Item:
    def __init__(self, name, value, weight, shelf_life):
        self.name = name
        self.value = value
        self.weight = weight
        self.shelf_life = shelf_life

    def __repr__(self):
        return f"Item({self.name}, value: {self.value}, weight: {self.weight}, shelf_life: {self.shelf_life})"

def fractional_knapsack(items, capacity):
    if capacity <= 0:
        return "Error: Vehicle capacity must be greater than 0."
    if any(item.shelf_life <= 0 for item in items):
        return "Error: Shelf life of items must be greater than 0."
    if sum(item.weight for item in items) <= capacity:
        return "Error: Total weight of items is less than or equal to zero."

    items.sort(key=lambda x: (x.value / x.weight) / x.shelf_life, reverse=True)
    total_value = 0.0
    total_weight_used = 0.0
    remaining_capacity = capacity
    selected_items = []

    for item in items:
        if remaining_capacity == 0:
            break
        if item.weight <= remaining_capacity:
            selected_items.append((item, 1))
            total_value += item.value
            total_weight_used += item.weight
            remaining_capacity -= item.weight
        else:
            fraction = remaining_capacity / item.weight
            selected_items.append((item, fraction))
            total_value += item.value * fraction
            total_weight_used += item.weight * fraction
            remaining_capacity = 0

    if total_value == 0:
        return "Error: No value could be obtained from the items."

    return total_value, total_weight_used, selected_items

items = [
    Item(f"Item_{i + 1}", random.randint(0, 1000), random.randint(10, 200), random.randint(10, 200))
    for i in range(100)
]
vehicle_capacity = 200

result = fractional_knapsack(items, vehicle_capacity)

if isinstance(result, str):
    print(result)
else:
    max_value, total_weight_used, selected_items = result
    print(f"Maximum profit achievable: {max_value:.2f} units")
    print(f"Total weight used: {total_weight_used:.2f} tons")
    print(f"Remaining capacity: {vehicle_capacity - total_weight_used:.2f} tons\n")
    print("Items selected:")

    header = (
        f"{'Item':<10} {'Fraction (%)':<15} "
        f"{'Weight (Selected/Total)':<25} {'Value (Selected/Total)':<25} "
        f"{'Shelf Life (days)':<15}"
    )
    print(header)
    print("-" * len(header))

    for item, fraction in selected_items:
        selected_weight = item.weight * fraction
        selected_value = item.value * fraction
        print(
            f"{item.name:<10} {fraction * 100:<15.1f} "
            f"{selected_weight:.2f}/{item.weight:<25} "
            f"{selected_value:.2f}/{item.value:<25} "
            f"{item.shelf_life:<15}"
        )
