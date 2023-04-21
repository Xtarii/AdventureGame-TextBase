"""
Här är Orch scripten

den delen som kommer att styra
vilka alternativ man har när
man blir attackerad av en orch

så vi behöver imports
"""
import os, styles, random
from Assets.Global_World import loot_tables





""" Här är functioner, alltså commandon på vad man kan göra """
class floridaMan():
    def __init__(self, player):
        self.player = player

        # Extras
        self.loot = loot_tables.loot_table(self.player)


    # Ta skydd från jordbävningen
    def taSkydd(self):
        """ Här tar vi skydd """
        os.system("cls")

        # Inledande text
        print(styles.Colors["GREEN"] + """
Jag ser en stor stubbe, så jag springer ditt.
Jag han backom stubben som tur var, "pust" """ + styles.Colors["FAIL"] + """

Tydligen kunde Orchen känna lukten av människor.
Han hittade mig backom stubben, jag fick springa för
mitt liv, han hann slå mig 2 gånger, fast en gång
i armen så jag förlorade bara 1 liv.
\n""")

        # tar skada
        self.player.takeDamage(1)





    # Tar en lista över vad man kan göra
    def kanGöra_skaparLista(self):
        lista = {
            1: {
                "text": (styles.Colors["GREEN"] +  "Ta Skydd"),
                "exe": self.taSkydd
            }
        }


        # Skapar en ny lista
        new_lista = {}

        # Tar random saker från "lista"
        for x in range(random.randint(1, 3)):
            list_index = random.randint(1, len(lista)) # Tar ett random numer från listan

            # Kollar om "lösningen" redan finns i listan, om inte lägger vi till lösning i listan
            t = new_lista.values()
            if lista[list_index] not in t:
                # Lägger till alternativ i listan
                new_lista.update({x:lista[list_index]})

        return new_lista





""" Här väljer vi ut några specifika saker som ska kunna göras """
def kanGöras(player):
    # Kallar på saker man kan göra
    fm = floridaMan(player)
    options_lista = fm.kanGöra_skaparLista()


    # Skapar en läsbar lista
    options = styles.Colors["GREEN"] + """
Vad ska jag göra:
=================
""" + styles.Colors["ENDC"]

    index = 0
    for x in options_lista:
        # Fixar options till display
        options += (
            styles.Colors["BLUE"] + str(index) + " : " +
            str(options_lista[x]["text"])
            + "\n" + styles.Colors["ENDC"]
        )

        # updaterar index
        index += 1

    # Vissar options
    print(options)
    # Input på vad man vill göra
    gör = input(styles.Colors["BLUE"] + "< Vad ska jag göra > ")

    # Testar att köra "exe" från input
    try:
        options_lista[int(gör)]["exe"]()
    except:
        print(styles.Colors["WARNING"] + """
Jag kom inte på något att göra i denna situationen,
så jag stod kvar. Flordia mannen boxade på mig
""" + styles.Colors["FAIL"] + """
Jag har beräknat att jag förlorade 1 liv eftersom
att jag inte kunde agera under press.
""" + styles.Colors["ENDC"])

        # Tar skada på player
        player.takeDamage(1)


    # En continue Delay
    input(styles.Colors["BLUE"] + "< continue >" + styles.Colors["ENDC"])
