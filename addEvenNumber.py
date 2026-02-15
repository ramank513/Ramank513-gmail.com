# Initialize the product at 1
total_product = 1

# Loop through even numbers from 50 to 60
# We use 61 because the end limit is exclusive
for num in range(50, 61, 2):
    total_product *= num
    print(f"Multiplying by {num}, current product: {total_product}")

print(f"\nThe final product of even numbers from 50 to 60 is: {total_product:,}")
