"""
Round floating-point numbers

Task: Given a floating-point number value
Round value to the nearest integer.
Round value to two decimal places.
value:float = 12.34567
Expected Output:
Rounded to nearest integer: 12
Rounded to two decimal places: 12.35
  """
  
# Given value
value = 12.34567

# Round to the nearest integer
rounded_integer = round(value)

# Round to two decimal places
rounded_two_decimal = round(value, 2)

# Print the results
print(f"Rounded to nearest integer: {rounded_integer}")
print(f"Rounded to two decimal places: {rounded_two_decimal}")
