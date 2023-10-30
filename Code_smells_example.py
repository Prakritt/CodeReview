#Code Smells Example for long method
def calculate_total_price(items):
    total = 0
    for item in items:
        total = total +  calculate_item_price(item)
    return total

def calculate_item_price(item):
    if item.quantity > 0:
        if item.price > 100:
            return item.quantity * item.price
    return 0