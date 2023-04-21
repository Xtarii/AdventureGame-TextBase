"""
Här är jordbävningen
alltså kommer allt man kan göra när en jordbävning händer, hända här

och för denna scripten behöver vi så klart "imports"
"""
import styles, os, random
from Assets.Global_World import loot_tables





""" Här är functioner, alltså commandon på vad man kan göra """
class jordbävning_Saker_Att_göra():
    def __init__(self, player):
        self.player = player

        # Extras
        self.loot = loot_tables.loot_table(self.player)


    # Ta skydd från jordbävningen
    def springTillPlatYta(self):
        """ Här tar vi skydd """
        os.system("cls")

        # Inledande text
        print(styles.Colors["GREEN"] + """
Jag ser slutet av skogen, så jag börjar springa.
Men jag ser en liten familj med ormar som
är i knippa, jag bestämmer dig för att rädda dem! Vilken hjälte.
Jag hinner ut med livet i behåll och ormarna i famnen.""" + styles.Colors["FAIL"] + """

Ormarna var giftiga, jag upptäkte det efter att dem attackerade mig.
Så otacksamma, detta gör jag aldrig om...eftersom att jag förlorade 1 hjärt!!!
\n""")

        # tar skada
        self.player.takeDamage(1)


    # Göm dig
    def gömDig(self):
        """ Här gömmer vi oss under ett bord """
        os.system("cls")

        # Inledande text
        print(styles.Colors["GREEN"] + """
Jag hittar ett bord att slänga mig under,
jag slänger mig under botder och skrapar upp armen
men det gör inget för det viktigaste är att
överleva just nu.
""" + styles.Colors["BLUE"] + """
Vilket geni jag är...det verkar inte vara en så
stark jordbävning så bordet verkar hålla!!!\n\n
""")
        # väntar på att jordbävningen ska gå över
        styles.loadLineDSE(text="Väntar på att det ska gå över:", sleep=0.01)

        # En continue Delay
        input(styles.Colors["BLUE"] + "< continue >" + styles.Colors["ENDC"])
        # Tar bort skräp på skärmen
        os.system("cls")

        # Avslutar
        print(styles.Colors["GREEN"] + """
Jag överlevde för en annan dag.
Dessutom gick det änkelt att komma ut eftersom
att inget hade gott sönder eller trillat.

Jag hittade dessutom något under bortdet,
så det var där min frukost hamnde...
        """ + styles.Colors["ENDC"])

        # lägger till "något" i inventory
        self.loot.common_loot(1)


    # Flygg iväg
    def flygg_iväg(self):
        """ Blir räddad av en drake """

        # Inledning
        print(styles.Colors["FAIL"] + """
Jag försökte flygga iväg men kom snabbt på att
jag inte har några vingar...""" + styles.Colors["WARNING"] + """
Jag tänkte just ge upp när en stor drake flög över
mig!!! Jag huckar mig ner för att inte bli synas!""" + styles.Colors["FAIL"] + """

Draken kunde tydligen känna lukten av mig och landade
framför mig. Vad tänkte jag på...du kommer den att
grilla mig!!!!!""" + styles.Colors["GREEN"] + """

Tydligen var draken mycket snäll, den sa att den såg
någon på marken som verkade vara i nöd, "pinsamt",
den berättade att den döck ner för att rädda mig.
Jag är mycket tacksam!!!!
        """)

        # Ge bort något till den
        print(styles.Colors["BLUE"] + "Som tack, vill jag gärna ge något till Draken.")

        # Skriver ut alla saker i inventory
        if self.player.inventory != []:
            for x in range(len(self.player.inventory)):
                print(str(x) + " : " + self.player.inventory[x])


            geBort = input(styles.Colors["GREEN"] + "Men vad? ")
            # Ger bort saken
            try:
                print(str(self.player.inventory[int(geBort)]) + """ är vad jag ska ge bort, det gillar nog draken!!!"""
                + styles.Colors["ENDC"])

                self.player.inventory.remove(self.player.inventory[int(geBort)])

            # Om man inte ger bort något
            except:
                print(styles.Colors["WARNING"] + """
Jag gav inte bort något, draken blev ledsen men
förstod. Den attackerade inte mig.
            """ + styles.Colors["ENDC"])

        else:
            print(styles.Colors["WARNING"] + """
Jag gav inte bort något, draken blev ledsen men
förstod. Den attackerade inte mig.
            """ + styles.Colors["ENDC"])





    # Tar en lista över vad man kan göra
    def kanGöra_skaparLista(self):
        lista = {
            1: {
                "text": (styles.Colors["GREEN"] +  "Spring till en plat yta!!!"),
                "exe": self.springTillPlatYta
            },

            2: {
                "text": (styles.Colors["GREEN"] + "Göm dig under något"),
                "exe": self.gömDig
            },

            3: {
                "text": (styles.Colors["CYAN"] + "Flyg till himlen!!!"),
                "exe": self.flygg_iväg
            }
        }


        # Skapar en ny lista
        new_lista = {}

        # Tar random saker från "lista"
        for x in range(random.randint(1, 2)):
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
    jsag = jordbävning_Saker_Att_göra(player)
    options_lista = jsag.kanGöra_skaparLista()


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
så jag stod kvar. Nu har jag ont i huvudet
eftersom att ett träd välte på mig
""" + styles.Colors["FAIL"] + """
Jag har beräknat att jag förlorade 2 liv eftersom
att jag inte kan ta ansvar över att överleva
i en jordbävning...
""" + styles.Colors["ENDC"])

        # Tar skada på player
        player.takeDamage(2)


    # En continue Delay
    input(styles.Colors["BLUE"] + "< continue >" + styles.Colors["ENDC"])
