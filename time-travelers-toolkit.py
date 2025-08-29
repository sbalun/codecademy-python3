from datetime import datetime as dt
from custom_module import generate_time_travel_message
from decimal import Decimal
from random import randint, choice, random

now = dt.now()
print(now)

dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("Current date and time:", dt_string)

base_cost = Decimal('1000.00')
current_year = now.year
target_year = 2030

year_difference = abs(target_year - current_year)
cost_multiplier = Decimal('1.05') ** year_difference

final_cost = base_cost * cost_multiplier
final_cost = final_cost.quantize(Decimal('0.01'))
print(f'Time travel cost: ${final_cost}')

# Define the range of possible years
start_year = 100
end_year = 2100

# Generate a random year within the range
target_year = randint(start_year, end_year)
print(f"The time travel target year is: {target_year}")

destinations = [
    "Rome, 100 AD – Height of the Roman Empire",
    "China, 800 AD – Tang Dynasty",
    "Machu Picchu, 1450 AD – Inca Empire",
    "Florence, 1500 AD – Renaissance",
    "Philadelphia, 1776 – U.S. Declaration of Independence",
    "New York, 1920 – Jazz Age",
    "Moon Landing, 1969",
    "Tokyo, 2100 – Futuristic Metropolis"
]

chosen_destination = choice(destinations)
print("Your time travel destination is:", chosen_destination)

message = generate_time_travel_message(target_year, chosen_destination, final_cost)
print(message)

print("\n🎉 Congratulations on completing your time travel project! 🚀")


