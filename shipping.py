
weight = 1.5
flatRate = 20.00
cost = 0.00

# Ground Shipping
if weight <= 2:
    cost = weight * 1.50 + flatRate
if weight > 2 and weight <= 6:
    cost = weight * 3.00 + flatRate
if weight > 6 and weight <= 10:
    cost = weight * 4.00 + flatRate
if weight > 10:
    cost = weight * 4.75 + flatRate
print(f"The price of ground shipping is: ${cost}")

# Ground Shipping Premium
cost = 125
print(f"The price of ground shipping premium is: ${cost}")

# Drone Shipping
if weight <= 2:
    cost = weight * 4.50
if weight > 2 and weight <= 6:
    cost = weight * 9.00
if weight > 6 and weight <= 10:
    cost = weight * 12.00
if weight > 10:
    cost = weight * 14.25
print(f"The price of drone shipping premium is: ${cost}")
