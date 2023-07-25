class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, name, amount=1):
        """
        Purpose: adds animal to the farm
        """
        for _ in range(amount):
            self.animals.append(name)
        print(f"{amount} {name}(s) were added to the farm")

    def get_animal_types(self):
        """
        Purpose: returns a sorted list of all animal types (names) in the farm
        """
        return sorted(set(self.animals))

    def get_short_info(self):
        """
        Purpose: returns a formatted string with farm name and animal types
        """
        animal_types = self.get_animal_types()
        animal_types_str = ", ".join(animal_types)
        return f"McDonald's farm has {animal_types_str}."

# Example usage:
farm = Farm()
farm.add_animal("cow", 2)
farm.add_animal("goat", 3)
farm.add_animal("sheep", 1)

info_string = farm.get_short_info()
print(info_string)  # Output: "McDonald's farm has cow, goat, sheep."
