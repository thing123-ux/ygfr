class Plant:
    def __init__(self, name, status="seed", height=0):
        self.name = name
        self.status = status
        self.height = height

    def care(self):
        if self.status in ["living", "seed"]:
            self.height += 10
            print(f"{self.name} was cared and grew 10cm (so cool!!!)")
        else:
            print(f"{self.name} unable to be cared because the plant's status is {self.status} (ts pmo...)")

    def sell(self):
        if self.status not in ["sold", "dead"]:
            self.status = "sold"
            print(f"{self.name} is now sold (free monehhh🤑🤑)")
            return max(0, self.height * 5)
        else:
            print(f"{self.name} cannot be sold (-12,493,234,135,235 social credit😨😨😨)")
            return 0

    def __str__(self):
        return f"{self.name} - status: {self.status}, height: {self.height}cm"

class Game:
    def __init__(self):
        self.plants = []
        self.money = 1000

    def add_plant(self, name):
        if self.money >= 200:
            self.money -= 200
            new_plant = Plant(name)
            self.plants.append(new_plant)
            print(f"added new {name} plant, moneh left: {self.money} vnd")
        else:
            print("haha u broke cant even afford a tree haha")

    def care_plant(self, name):
        for plant in self.plants:
            if plant.name == name:
                plant.care()
                return
        print("invalid response")

    def sell_plant(self, name):
        for plant in self.plants:
            if plant.name == name:
                profit = plant.sell()
                self.money += profit
                print(f"u just profited {profit} vnd. total monehh: {self.money}")
                return
        print("invalid response")

    def show_plants(self):
        print("\n--- list of plants ---")
        for plant in self.plants:
            print(plant)
        print(f"total monehh: {self.money} vnd\n")

game = Game()
game.add_plant("daffodil")
game.care_plant("daffodil")
game.sell_plant("daffodil")
game.show_plants()
