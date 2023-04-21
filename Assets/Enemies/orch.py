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
class orch_attack_kan_göra():
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


    # Göm dig
    def spring(self):
        """ Här springer vi iväg """
        os.system("cls")

        # Inledande text
        print(styles.Colors["GREEN"] + """
Jag börjar springa allt vad jag har.
Som tur är är Orcher mycket långsamma, så
han kan inte följa efter mig.""" + styles.Colors["BLUE"] + """

Jag set att Orchen skratar och pekar på mig,
han verkar inte veta att jag kommer undan -
HA HA HA HA.
\n\n
""")

        # väntar på att jordbävningen ska gå över
        styles.loadLineDSE(text="Springer in i ett berg", sleep=0.01)

        # En continue Delay
        input(styles.Colors["BLUE"] + "< continue >" + styles.Colors["ENDC"])
        # Tar bort skräp på skärmen
        os.system("cls")

        # Avslutar
        print(styles.Colors["WARNING"] + """
Han stannade tydligen för berget som jag missade att se.
Jag sprang rakt in i det...

Jag gjorde illa mig men förlorade inga hjärtan!!!
Vilken tur, och jag hittade en grotta!!!
        \n\n""" + styles.Colors["ENDC"])


        # Går kanske in i grottan
        print(styles.Colors["WARNING"] + "0 : Gå inte in i grottan det kan finnas monster!!!")
        print(styles.Colors["FAIL"] + "1 : Gå in i grottan, det kan vara spänande!!!")
        # Svar och rensar skärmen
        svar = input(styles.Colors["BLUE"] + "Vad vill jag göra?: > " + styles.Colors["ENDC"])
        os.system("cls")


        # Om man klickar på 1 så går man in i grottan
        if svar == "1":
            # Skriver vad man hittade
            print(styles.Colors["GREEN"] + """
Det var inga monster i grottan, men
mitt i grottan var en stor kista i rent
guld, jag öppnade den och hittade:
            """)

            # lägger till det du hittade i inventory
            self.loot.rare_loot(4)
            self.loot.common_loot(2)


        # Om man inte går in i grottan
        else:
            print(styles.Colors["GREEN"] + """
Jag gick inte in i grottan,
det var nog för det bättre bra
            """)


    # Flygg iväg
    def ge_gåva(self):
        """ Ger något till orchen """

        # Inledning
        print(styles.Colors["FAIL"] + """
Jag borde ge något till orchen.
""" + styles.Colors["WARNING"] + """
Orchen närmar sig snabbt, men jag stor kvar med
minna ord, jag letar efter något att ge bort.""" + styles.Colors["FAIL"] + """

Men vad ska jag ge bort!!! Det börjar bli
ont om tid att komma på något
""")

        # Ge bort något till den
        print(styles.Colors["BLUE"] + "Jag öppnar min ryggsäck,")

        # Skriver ut alla saker i inventory
        if self.player.inventory != []:
            for x in range(len(self.player.inventory)):
                print(str(x) + " : " + self.player.inventory[x])


            geBort = input(styles.Colors["GREEN"] + "Vad ska ges bort? ")
            # Ger bort saken
            try:
                print(str(self.player.inventory[int(geBort)]) + """ är vad jag ska ge bort, hoppas orchen gillar det!!!"""
                + styles.Colors["ENDC"])

                self.player.inventory.remove(self.player.inventory[int(geBort)])


            # Om man inte ger bort något
            except:
                print(styles.Colors["WARNING"] + """
Orchen fortsatte att springa, och eftersom att inget
var i mitt inventor så van orchen denna gången.

Han stoppade mig i en gryta och tände eld.
Det blev så varmt att jag gav upp hoppet :(
            """ + styles.Colors["ENDC"])

                # Avslutar spelet
                os.sys.exit(0)

        else:
            print(styles.Colors["WARNING"] + """
Orchen fortsatte att springa, och eftersom att inget
var i mitt inventor så van orchen denna gången.

Han stoppade mig i en gryta och tände eld.
Det blev så varmt att jag gav upp hoppet :(
            """ + styles.Colors["ENDC"])

            # Avslutar spelet
            os.sys.exit(0)



    # Roppa på hjälp
    def roppaPåHjälp(self):
        print(styles.Colors["CYAN"] +
        """
Jag Roppar så högt jag kan på hjälp...""" + styles.Colors["FAIL"] + """
HJÄLP!!!!, EN ORCH!!!!, HJÄLP!!!!""" + styles.Colors["CYAN"] + """

Det verkar som att några ridare hörde mig.
Jag är räddad från det monster som står framför mig.
""" + styles.Colors["GREEN"] + """
De börjar springa hit, det är 10 stycken riddare.
De Drar sina svärd mot Orchen som återvänder till
sitt mörka bo. Dem gav mig en sälsynt gåva så att jag
kan förbli säker i fortsättningen.
        """ + styles.Colors["ENDC"])

        # Lägger till en random loot i inventoryt
        self.loot.rare_loot(1)





    # Tar en lista över vad man kan göra
    def kanGöra_skaparLista(self):
        lista = {
            1: {
                "text": (styles.Colors["GREEN"] +  "Ta Skydd"),
                "exe": self.taSkydd
            },

            2: {
                "text": (styles.Colors["GREEN"] + "Spring!!!"),
                "exe": self.spring
            },

            3: {
                "text": (styles.Colors["CYAN"] + "Ge något till orchen?"),
                "exe": self.ge_gåva
            },

            4: {
                "text": (styles.Colors["BLUE"] + "Roppa på hjälp!"),
                "exe": self.roppaPåHjälp
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
    oakg = orch_attack_kan_göra(player)
    options_lista = oakg.kanGöra_skaparLista()


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
så jag stod kvar. Orchen Slängde sin yxa på mig
""" + styles.Colors["FAIL"] + """
Jag har beräknat att jag förlorade 1 liv eftersom
att jag inte kunde agera under press.
""" + styles.Colors["ENDC"])

        # Tar skada på player
        player.takeDamage(1)


    # En continue Delay
    input(styles.Colors["BLUE"] + "< continue >" + styles.Colors["ENDC"])
