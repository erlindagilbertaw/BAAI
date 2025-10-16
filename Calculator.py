# PRODUCT DISCOUNT CALCULATOR

products = [
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "Shirt", "price": 45, "category": "Clothing"},
    {"name": "Phone", "price": 800, "category": "Electronics"},
    {"name": "Shoes", "price": 120, "category": "Clothing"},
    {"name": "Tablet", "price": 350, "category": "Electronics"},
    {"name": "Jacket", "price": 95, "category": "Clothing"},
    {"name": "Book", "price": 25, "category": "Books"},
    {"name": "Headphones", "price": 150, "category": "Electronics"}
]

# Initialize tracking variables
total_original = 0
total_discount_amount = 0
total_final = 0
total_discount_rate = 0

max_discount_product = None
max_discount_amount = 0
max_discount_rate = 0

category_count = {}  
most_expensive_product = None  
cheapest_product = None        
highest_final_price = 0        
lowest_final_price = float("inf")

print("\033[1m=== PRODUCT DISCOUNT CALCULATOR ===\033[0m\n")

# Process each product
for PRODUCT in products:
    NAME = PRODUCT["name"]
    PRICE = PRODUCT["price"]
    CATEGORY = PRODUCT["category"]

    # Determine discount based on category and price
    if CATEGORY == "Electronics":
        if PRICE >= 1000:
            discount_rate = 0.20
        elif PRICE >= 500:
            discount_rate = 0.15
        else:
            discount_rate = 0.10
    elif CATEGORY == "Clothing":
        if PRICE >= 100:
            discount_rate = 0.25
        else:
            discount_rate = 0.15
    elif CATEGORY == "Books":
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    # Calculate final price
    discount_amount = PRICE * discount_rate
    final_price = PRICE - discount_amount

    # Product total details
    total_original += PRICE
    total_discount_amount += discount_amount
    total_final += final_price
    total_discount_rate += discount_rate

    # Count products by category
    category_count[CATEGORY] = category_count.get(CATEGORY, 0) + 1

    # Check highest discount
    if discount_amount > max_discount_amount:
        max_discount_amount = discount_amount
        max_discount_product = PRODUCT
        max_discount_rate = discount_rate

    # Check most expensive and cheapest product after discount
    if final_price > highest_final_price:
        highest_final_price = final_price
        most_expensive_product = PRODUCT

    if final_price < lowest_final_price:
        lowest_final_price = final_price
        cheapest_product = PRODUCT

    # Add Clearance Tag with emoji if discount >= 20%
    tag = "🔥" if discount_rate >= 0.20 else ""

    # Print product details
    print(f"Product: {NAME}{tag}")
    print(f"Category: {CATEGORY}")
    print(f"Original Price: ${PRICE:.2f}")
    print(f"Discount: {int(discount_rate * 100)}%")
    print(f"Final Price: ${final_price:.2f}\n")

# Calculate average discount rate
average_discount_rate = (total_discount_rate / len(products)) * 100

print()
print()

# Print summary
print("\033[1m=== SUMMARY ===\033[0m")
for category, count in category_count.items():
    print(f"{category}: {count} product(s)")
print(f"Total Products: {len(products)}")
print()
print(f"Total Original Price: ${total_original:.2f}")
print(f"Total Discount: ${total_discount_amount:.2f}")
print(f"Total Final Price: ${total_final:.2f}")
print(f"Average Discount Rate: {average_discount_rate:.2f}%\n")
print(f"Total Savings for Customer: ${total_discount_amount:.2f}")

print()
print()

# Print product with highest discount
print("\033[1m=== HIGHEST DISCOUNT PRODUCT ===\033[0m")
print(f"Product: {max_discount_product['name']}")
print(f"Category: {max_discount_product['category']}")
print(f"Original Price: ${max_discount_product['price']:.2f}")
print(f"Discount: {int(max_discount_rate * 100)}%")
print(f"Discount Amount: ${max_discount_amount:.2f}\n")

print()
print()

# Print most expensive and cheapest product after discount
print("\033[1m=== MOST EXPENSIVE & CHEAPEST PRODUCTS AFTER DISCOUNT ===\033[0m")
print(f"Most Expensive: {most_expensive_product['name']} (${highest_final_price:.2f})")
print(f"Cheapest: {cheapest_product['name']} (${lowest_final_price:.2f})")