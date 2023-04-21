"""
Här är player.
allt som händer med player kommer att tas hand om här typ.

imports för att få en finnare script
"""
import styles, time, os



# Här är player class
class Player():
    def __init__(self, health: int, inventory_capasity: int):
        # Players liv
        self.health = int(health)

        # Players inventory
        self.inventory_capasity = int(inventory_capasity)
        self.inventory = []


    # Update, detta kommer att köra varje "runda i while loopen"
    def Update(self):
        """ Player Update för att updatera player """

        # Kollar om spelaren har "dött"
        if self.health <= 0:
            """ Skapar en döds "scene" innan man dör """
            print(styles.Colors["WARNING"] + """
Jag o..or..kar inte...for..sätta, jag är så
sk..a..dad att varje.........and...e...e tag är en
....plåga. """ + styles.Colors["FAIL"] + """

Du lägger dig ned på marken och somnar för
att aldrig vakna igen.
            """ + styles.Colors["ENDC"])


            # En continue Delay
            input(styles.Colors["BLUE"] + "< continue >" + styles.Colors["ENDC"])
            # Avslutar programmet
            os.sys.exit(0)


    # Tar skada från spelaren
    def takeDamage(self, damage):
        """ Skadar spelaren """
        self.health -= int(damage)


    # Lägger till object i ett inventory om det inte är fullt
    def addToInventory(self, item: str):
        """ Lägger till "item" i players inventory """
        if len(self.inventory) != self.inventory_capasity:
            self.inventory.append(str(item))

            # Debug och visual effect för inventory
            print(styles.Colors["CYAN"] + "La till: " + str(item) + " i mitt inventory")
