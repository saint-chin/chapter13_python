purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(purchases):
    total = 0
    for p in purchases:
        total += p["price"] * p["quantity"]
    return total


print(total_revenue(purchases))


def items_by_category(purchases):
    categories = {}
    for p in purchases:
        item = p["item"]
        category = p["category"]

        if category not in categories:
            categories[category] = []

        categories[category].append(item)

    return categories


print(items_by_category(purchases))


def expensive_purchases(purchases, min_price):
    list_of_purchases = [p for p in purchases if p["price"] >= min_price]
    return list_of_purchases


print(expensive_purchases(purchases, 1.0))


def average_price_by_category(purchases):
    average_price = {}
    for p in purchases:
        category = p["category"]
        price = p["price"]
        if category not in average_price:
            average_price[category] = []
        average_price[category].append(price)
    for key, value in average_price.items():
        new_val = sum(value)
        average = new_val/len(value)
        average_price[key] = average
    return average_price


print(average_price_by_category(purchases))


def most_frequent_category(purchases):
    categories = {}
    for p in purchases:
        qty = p["quantity"]
        category = p["category"]

        if category not in categories:
            categories[category] = []

        categories[category].append(qty)

    for key, value in categories.items():
        new_val = sum(value)
        categories[key] = new_val

    return max(categories)


print(most_frequent_category(purchases))
