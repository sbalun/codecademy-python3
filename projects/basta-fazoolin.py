class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        # Human-friendly string representation
        return f"{self.name} menu available from {self._format_time(self.start_time)} to {self._format_time(self.end_time)}"

    def _format_time(self, t):
        # Formats integer times like 1100 as "11:00am"
        hour = t // 100
        minute = t % 100
        suffix = "am" if hour < 12 or hour == 24 else "pm"
        hour12 = hour % 12
        if hour12 == 0:
            hour12 = 12
        return f"{hour12}:{minute:02d}{suffix}"

    def calculate_bill(self, purchased_items):
        """
        Calculate the total cost of the given purchased item names.

        purchased_items: list[str] — names of items to buy
        Returns: float/int — total price of all found items
        """
        total = 0
        for item_name in purchased_items:
            price = self.items.get(item_name)
            if price is not None:
                total += price
            # If an item isn't found in the menu, it's ignored.
        return total

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f"We are located at {self.address}."

    def available_menus(self, time):
        """
        Return a list of Menu objects available at the given time (e.g., 1100).
        """
        available = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available.append(menu)
        return available

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __repr__(self):
        return f"{self.name} (Franchises: {len(self.franchises)})"

brunch = Menu("brunch", {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
},1100,1600)

early_bird = Menu("early_bird", {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00
},1500,1800)

dinner = Menu("dinner", {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00
},1700,2300)

kids = Menu("kids", {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
},1100,2100)

# Test menu early_bird
print(early_bird)

# Breakfast order: pancakes, home fries, and coffee
breakfast_order = ["pancakes", "home fries", "coffee"]
total_price = brunch.calculate_bill(breakfast_order)
print(f"Brunch order total: ${total_price:.2f}")

# early_bird order: salumeria plate, mushroom ravioli (vegan)
early_bird_order = ["salumeria plate", "mushroom ravioli (vegan)"]
total_price = early_bird.calculate_bill(early_bird_order)
print(f"Early Bird order total: ${total_price:.2f}")

# Create the flagship store
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner,kids])

# Create a new franchise location
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner,kids])

print(flagship_store)

# Menus available at 12pm
menus_available = new_installment.available_menus(1200)
print(f"Menus available at 12pm {menus_available}")

# Menus available at 5pm
menus_available = new_installment.available_menus(1700)
print(f"Menus available at 5pm {menus_available}")

# Create a new business
basta_fazoolin_business = Business("Basta Fazoolin' with my Heart",[flagship_store, new_installment])

# create a new menu
arepas_menu =  Menu("Arepas", {
  'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
},1000, 2000)

# Create a new franchise, arepas_place
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Create a new business with the new franchise
new_business = Business("Take a' Arepa", [arepas_place])
print(new_business)