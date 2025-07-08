def nth_highest_order(orders, n):
    # Get unique order counts and sort them in descending order
    unique_orders = sorted(set(orders.values()), reverse=True)
    
    # Check if n is valid
    if n > len(unique_orders) or n <= 0:
        return f"Invalid input: n = {n} is out of range."
    
    # Get the nth highest order count
    nth_highest = unique_orders[n - 1]
    
    # Find customers with the nth highest order count
    customers = [customer for customer, order_count in orders.items() if order_count == nth_highest]
    
    return nth_highest, customers

# Example dataset: customer ID -> number of orders
customer_orders = {
    "C001": 15,
    "C002": 20,
    "C003": 10,
    "C004": 20,
    "C005": 25,
    "C006": 15
}

# Find the 2nd highest number of orders
n = 2
result = nth_highest_order(customer_orders, n)

if isinstance(result, tuple):
    nth_highest, customers = result
    print(f"The {n}th highest number of orders is {nth_highest}.")
    print(f"Customers with {nth_highest} orders: {', '.join(customers)}")
else:
    print(result)
