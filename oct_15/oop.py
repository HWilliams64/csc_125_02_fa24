class Backpack:
    color = "white"         # Color of the backpack
    brand = "Jansport"      # Brand of the backpack
    capacity = 10           # Maximum capacity of the backpack
    allocated = 0           # The total items in the backpack

    def add_item(self, item) -> bool:
        # Check if the backpack has reached its capacity
        if self.allocated < self.capacity:

            # Add the item to the backpack if not at capacity and return True
            self.allocated += 1
            return True

        # Backpack is at capacity, no new item added, return False
        return False

    def remove_item(self, item) -> bool:
        # If there is at least one item in the backpack
        if self.allocated > 0:
            # Remove the item from the backpack and return True
            self.allocated -= 1
            return True
        # There are no items in the backpack, return False
        return False

my_backpack = Backpack()
print(f"My Backpack Color: {my_backpack.color}")
print(f"My Backpack Brand: {my_backpack.brand}")

your_backpack = Backpack()
print(f"Your Backpack Color: {your_backpack.color}")
print(f"Your Backpack Brand: {your_backpack.brand}")

print("=" * 80)

my_backpack.color = "blue"
your_backpack.color = "black"
print(f"My Backpack Color: {my_backpack.color}")
print(f"Your Backpack Color: {your_backpack.color}")

print("=" * 80)

my_backpack.add_item("Book")
print("was item added? ",your_backpack.add_item("Computer"))
print("was item added? ", your_backpack.add_item("Notebook"))
print("was item added? ", your_backpack.add_item("Wallet"))

for _ in range(10):
    print("\twas item added? ", your_backpack.add_item("book"))

print(f"My Backpack Items: {my_backpack.allocated}")
print(f"Your Backpack Items: {your_backpack.allocated}")

print("=" * 80)
print("was item removed? ", your_backpack.remove_item("Wallet"))
print(f"Your Backpack Items: {your_backpack.allocated}")
