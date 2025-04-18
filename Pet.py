class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        print(f"Creating pet: {self.name}")
    def eat(self):
        print(f"{self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy >= 2:
            print(f"{self.name} is playing...")
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
        else:
            print(f"{self.name} is too tired to play. Let them rest ")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}! ")
        else:
            print(f"{self.name} already knows how to {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks if self.tricks else 'No tricks learned yet'}\n")
