def calculate_discount(price, discount_percent):
    # Apply discount only if discount is 20% or higher
    if discount_percent >= 20:
        return price - (price * (discount_percent / 100))
    else:
        return price

# Example values for testing
price = 100.0  # Example original price
discount_percent = 25.0  # Example discount percentage

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price or original price if no discount applied
if discount_percent >= 20:
    print(f'The final price after applying the discount is: ${final_price:.2f}')
else:
    print(f'No discount applied. The original price is: ${price:.2f}')
