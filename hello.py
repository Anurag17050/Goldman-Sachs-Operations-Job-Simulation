import random

def get_random_number(start=1, end=100):
    """Return a random integer between start and end."""
    return random.randint(start, end)

def get_random_choice():
    """Return a random choice from a sample list."""
    items = ["apple", "banana", "cherry", "mango", "orange"]
    return random.choice(items)

if __name__ == "__main__":
    print("🎲 Random number between 1 and 100:", get_random_number())
    print("🍎 Random fruit choice:", get_random_choice())

