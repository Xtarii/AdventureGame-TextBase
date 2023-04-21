"""
Här genererar vi random loot
alltså en loot_table


vi börjar med imports
"""
import os, random



""" Här är själva classen för loot """
class loot_table():
    def __init__(self, player):
        self.player = player



    # En liten änkel vanlig loot table
    def common_loot(self, amount: int):
        vanlig_loot = ["äpple", "bannan", "pinne", "löv", "röd ros"]

        # Hur många gånger som loopen ska köras
        loot_amount = random.randint(1, amount)

        # Väljer en random loot från "vanlig loot"
        for x in range(loot_amount):
            # Väljer en random loot
            random_loot = random.randint(0, (len(vanlig_loot) - 1))
            self.player.addToInventory(vanlig_loot[random_loot])



    # En liten änkel vanlig loot table
    def rare_loot(self, amount: int):
        ovanlig_loot = ["Svärd (Dvärg)", "Svärd (Elvor)", "Obsidian röstning (Dvärg)", "Tandpetare", "ros av guld"]

        # Hur många gånger som loopen ska köras
        loot_amount = random.randint(1, amount)

        # Väljer en random loot från "vanlig loot"
        for x in range(loot_amount):
            # Väljer en random loot
            random_loot = random.randint(0, (len(ovanlig_loot) - 1))
            self.player.addToInventory(ovanlig_loot[random_loot])



    # En liten änkel vanlig loot table
    def water_loot(self, amount: int):
        vatten_loot = ["Triteons Stav", "Snäckor", "Gummistövel", "Räckor", "Magisk Pärla", "Båt",
        "Flaks båt", "Sjöjungfru", "Trireons Krona", "Skelet"]

        # Hur många gånger som loopen ska köras
        loot_amount = random.randint(1, amount)

        # Väljer en random loot från "vanlig loot"
        for x in range(loot_amount):
            # Väljer en random loot
            random_loot = random.randint(0, (len(vatten_loot) - 1))
            self.player.addToInventory(vatten_loot[random_loot])



    # Guld och andra värdefulla saker
    def guld_och_annat(self, amount):
        dyrt_loot = ["Guld Klimpar", "Pengar", "Körkort", "ID", "Diamanter"]

        # Hur mycket loot det ska vara
        loot_amount = random.randint(1, amount)

        # Väljer random dyrt loot
        for x in range(loot_amount):
            # Väljer random från listan "dyrt_loot"
            random_loot = random.randint(0, (len(dyrt_loot) - 1))
            self.player.addToInventory(dyrt_loot[random_loot])
