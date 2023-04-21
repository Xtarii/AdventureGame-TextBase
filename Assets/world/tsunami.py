"""
Här är tsunamin
alltså kommer allt man kan göra när en tsunami kommer, hända här

och för denna scripten behöver vi så klart "imports"
"""
import styles, os, random
from Assets.Global_World import loot_tables





""" Här är functioner, alltså commandon på vad man kan göra """
class tsunami():
    def __init__(self, player):
        self.player = player

        # Extras
        self.loot = loot_tables.loot_table(self.player)


    # Ta skydd från jordbävningen
    def springTillPlatYta(self):
        """ Här tar vi skydd """
        os.system("cls")

        # Inledande text
        print(styles.Colors["FAIL"] + """
Jorden börjar skaka, en stor våg är på väg!!!!
Jag börjar springa, den närmar sig snabbt.
Hoppet är ute, den är så snabb och långsam,
""" + styles.Colors["GREEN"] + """
Jag ser ett berg, jag tar chansen och springer
dit, jag tror jag kan hinna....

En dam var i vägen, jag knuffade henne och
fortsatte att springa, jag hinner.

Wohoo jag han, jag han. Damen är borta
men vem bryr sig jag han.\n""" + styles.Colors["ENDC"])

        # En continue Delay
        input(styles.Colors["BLUE"] + "< continue >" + styles.Colors["ENDC"])

        # Efter tsunamin
        print(styles.Colors["WARNING"] + """
En familj närmar sig mig,

- Har du set våran mormor, hon är kort
och senil. Hon var påväg upp hit.
        """ + styles.Colors["ENDC"])

        # Ska du erskänna eller inte
        print(styles.Colors["FAIL"] + """
0 : Ljug""" + styles.Colors["BLUE"] + """
1 : Berätta sanningen
        """ + styles.Colors["ENDC"])

        svar = input(styles.Colors["WARNING"] + "Vad ska jag göra? ")

        # Väljer ditt öde
        if svar == "1":
            print(styles.Colors["GREEN"] + """
Jag berättade sanningen, det kändes bra att inte
ljuga för den stakars familjen. Jag kan äntligen
leva resten av mitt liv med frid och fröjd.""" + styles.Colors["FAIL"] + """

Dem kallade mig för monster, och sa att jag skulle
brina i flera hundra år i helvetet. Jag förstod
varför, men ändå, dem var så duma mot mig.""" + styles.Colors["WARNING"] + """

Så jag sa till dem att den gamla hagan hade ändå
inte klarat sig upp för berget och dem borde
tacka mig...""")

            # En continue Delay
            input(styles.Colors["BLUE"] + "< continue >" + styles.Colors["ENDC"])
            os.system("cls")

            # Drama
            print(styles.Colors["FAIL"] + """
Just då slog en våg upp damens mycket skadade
kropp på berget där vi alla stod. Den var mycket
skadad och många kropsdelar var avslitna.
Hennes Familj började gråtta, en av dem spyde
till och med.

En av dem slog mig, och en annan spottade på mig.
Polisen kom och hämtade mig, jag förlorade i domstolen
eftersom att någon tydligen filmade mig när jag
gjorde det. Jag fick 10000 år i fängelset eftersom att
jag är i USA. Jag dog i fängelset.
            """ + styles.Colors["ENDC"])

            # Delay
            input(styles.Colors["BLUE"] + "< continue >" + styles.Colors["ENDC"])

            print(styles.Colors["WARNING"] + """
Jag gav upp mitt liv på toppen och ångrar inget,
den mormorn förtjänade att dö, hennes familj
var ju duma mot mig. Jag kom till helvetet dock.
            """)
            # Avslut
            os.sys.exit(0)

        else:
            print(styles.Colors["WARNING"] + """
Jag ljög och sa att jag inte hade sett henne.
En våg sjöljde upp henne på berget och alla började
gråta, jag tvingade fram lite tårer så att ingen
skull misstänka mig. Det fungerade och
familjen tackade för min hjälp fast att jag inte
gjorde något, dem måste ha varit Svenskar.

Jag lyckades dock råna deras kära lilla senila mormor
på en massa bra saker.
            """ + styles.Colors["ENDC"])

            # Lastar mina fickor med guld och loot
            styles.loadLineDSEL(0.01, "Lämnar saker i mitt inventory: ")
            self.loot.common_loot(1)
            self.loot.rare_loot(1)
            self.loot.guld_och_annat(3)


    # Gå runt
    def gåRunt(self):
        print(styles.Colors["GREEN"] + """
Tsunamin verkar inte vara så lång, om jag
går snet så kanske jag kan lyckas gå runt
den. """ + styles.Colors["BLUE"] + """
Det är mycket i vägen. Men efter en liten
stund lyckades jag åkta runt tsunamin.

Jag är fri och hel.
        """ + styles.Colors["ENDC"])


    # Stopa vågen
    def sägStop(self):
        print(styles.Colors["WARNING"] + """
Vågen närmar sig, vågar (haha) jag stopa den,
den kan vara ett självmords uppdrag
och jag tror ingen någonsin är såpass riskfylld
som jag är nu.

Jag sätter upp handen i luften och säger:
- STOP, STOOOP!!!!!


Till min förvåning stannar vågen och och säger:
- Förlåt lilla människa, jag blev så arg
bara. Jag ville hämnas min kompis "Flint the Fish"


Tsunamin lugnar sig själv och gav mig en gåva.
        """ + styles.Colors["ENDC"])

        # lägger till gåva i mitt inventory
        self.loot.water_loot(1)
        # Delay
        input(styles.Colors["BLUE"] + "< continue >" + styles.Colors["ENDC"])
        os.system("cls")

        # Avslut
        print(styles.Colors["CYAN"] + """
Han berättar en lång historia om hur några fisakre
fiskade upp hans kompis och jag avbrött han och sa
att det var en tragiskt historia, han sa att den inte
hade börjat än. Men jag fortsatte och sa att oavsett
vad en människagör så kan han inte attackera
alla människor.

Han ångrade att han gav mig en gåva, men tog inte
tillbacka den.
Vilken underlig våg, han måste ha en sjö-rvig (jag måste
sluta med alla sjö-na skämt, tänker jag)
hjärna eftersom att han var mycket konstig.
        """ + styles.Colors["ENDC"])


    # Stå kvar
    def ståKvar(self):
        print(styles.Colors["BLUE"] + """
Jag väljer att stå kvar eftersom att tsunamin är
typ 100 mil bort, och jag är uppe i ett torn.
Så den skulle aldrig nå fram till mig.


Jag står och dansar fortnite danser fram till
typ 22:00 på kvällen när en vakt får bära bort mig.

En ängel sa att det var smakt löst att dansa vinnar
danser åt folk som är i fara.
        """ + styles.Colors["ENDC"])


    # Kör iväg
    def körIväg(self):
        # Kör iväg med en bil
        print(styles.Colors["WARNING"] + """
Medans tsunamin närmar sig såg jag mig omkring
efter något användbar som typ en bil eller en helikopter.
Jag måste hitta något fort!!! """ + styles.Colors["GREEN"] + """

HAHA, bingo jag hittade en lastbil, jag har ett
lastbilskörkort, så jag kan använda den för att ta mig här
ifrån.""" + styles.Colors["BLUE"] + """
Så jag hoppade in i lastbilen och började köra, men något är
konstigt med bilen, den typ guppar extra mycket. Det är svårt
att ha kontroll över flaket, det guppar jätte mycket!!!
        """ + styles.Colors["ENDC"])

        # Stannar lastbilen
        styles.loadLineDSEL(0.01, "Försöker stanna lastbilen: ")
        # En continue Delay
        input(styles.Colors["BLUE"] + "< continue >" + styles.Colors["ENDC"])
        os.system("cls")

        # Skriver ut part 2
        print(styles.Colors["FAIL"] + """
Jag råkade krocka med ett träd, men som tur var så hade lastbilen
krock-kuddar så jag klarade mig utan en skroma. Men det visade
sig att lastbilen var full med vodka, och det var därför det
var svårt att kontrollera vart jag körde.""" + styles.Colors["BLUE"] + """Jag fick iallafall stop
på lastbilen, och jag han undan tsunamin, men jag blev gripen av
polisen för misstänkt smugling och stöld av 10 ton vodka.

Jag förklarade hur det låg till med tsunamin och dem sa:
- No shit att det var en tsunami Sherlook!

Det hela slutade med att jag fick ta ut 1 års fängelsestraff
eftersom att jag tekniskt sett snodde lastbilen, och på det
fick jag en böter på 1000 kr - ouch! Men jag överlevde och
ibland är det, det viktigaste.
        """ + styles.Colors["ENDC"])


    # Ta en cykel
    def taCykel(self):
        print(styles.Colors["GREEN"] + """
Jag ser en cykel en liten bit härifrån, jag springer dit
och tar den så att jag kan cykla ifrån tsunamin.
Den var inte låst så medans tsunamin närmar sig kan jag i
lung och ro cykla ifrån tsunamin - eller kanske med lite fart!
Jag missuppfatade avståndet mellan den och mig. """ + styles.Colors["BLUE"] + """

Jag börjar cykla, och jag slänger av mig alla kläder
bara för att jag kan. Mitt skägg hänger ut över min kropp och
det fladrar i vinden. En liten flicka som jag cyklar förbi skricker:
- Mamma, mamma. Kolla där det är florida Jesus!!! Han kommer
för att kidnappa mig!!!


Jag fortsatte att cykla och klarade mig från tsunamin utan problem.
Jag googlade senare på Florida Jesus och ångrade mitt beslut att
cykla utan kläder. Men inget dåligt hände.

Florida Jesus:
https://www.boredpanda.com/funny-florida-jokes-memes-floridaman/?utm_source=google&utm_medium=organic&utm_campaign=organic
        """ + styles.Colors["ENDC"])


    # Låtsas vara en sten, man gömmer sig i en handduk
    def användHanduken(self):
        print(styles.Colors["WARNING"] + """
Jag tar snabbt min strandhandduk och sveper in mig i den. Jag låtsas
vara en stor sten som vågen inte kan flytta. """ + styles.Colors["GREEN"] + """ Vågen sköljer över mig
men jag känner mig trygg och säker i min lilla handduksgrotta.
        """ + styles.Colors["ENDC"])


    # KATTER!!!!
    def katter(self):
        print(styles.Colors["GREEN"] + """
Jag springer förbi några katter som är fast,
vad ska jag göra?
        """ + styles.Colors["ENDC"])

        print(styles.Colors["GREEN"] + """
0 : Jag ska rödda dem, men fort!!!
1 : Lämna dem, jag har nog med Katt-astrofer just nu!!!
        """ + styles.Colors["ENDC"])

        # Vad ska man göra
        svar = input(styles.Colors["WARNING"] + "Vad ska jag göra? ")
        os.system("cls")
        # Om man inte räddar dem:
        if(svar == "1"):
            print(styles.Colors["FAIL"] + """
Jag valde att läman dem, jag slängde salt-vatten
i ögonen för att folk skulle tro att jag grätt över
mitt beslut att överlämna dem.""" + styles.Colors["BLUE"] + """
Men jag överlede och det var det viktigaste, så jag
är lycklig!!! För jag tog mig upp på ett berg som
tsunamin drabbade.
            """ + styles.Colors["ENDC"])

        else:
            print(styles.Colors["GREEN"] + """
Jag valde att rädda dem små kryppen så att tsunamin
inte skulle få dem.""" + styles.Colors["WARNING"] + """ Dem rev mig flera gånger och en av
dem hade rabies, men det var värt det, jag förlorade
bara 1 liv och kunde leva resten av mitt liv med titeln:
- Hjälte för alla.

Men innan jag lämnar jorden så har jag fler uppdrag och
annat att göra, som att hjälpa den där gamla
damen att slå den där hemlössa gentelmannen bara för att
han gick brevid henne. Skurkar haa, dem är så jobbiga.
            """ + styles.Colors["ENDC"])
            # Tar bort 1 liv
            self.player.takeDamage(1)





    # Tar en lista över vad man kan göra
    def kanGöra_skaparLista(self):
        lista = {
            1: {
                "text": (styles.Colors["GREEN"] +  "Spring till en plat yta!!!"),
                "exe": self.springTillPlatYta
            },

            2: {
                "text": (styles.Colors["CYAN"] + "Gå runt tsunamin?..."),
                "exe": self.gåRunt
            },

            3: {
                "text": (styles.Colors["WARNING"] + "Säg stop till vågen..."),
                "exe": self.sägStop
            },

            4: {
                "text": (styles.Colors["FAIL"] + "Stå kvar på min position."),
                "exe": self.ståKvar
            },

            5: {
                "text": (styles.Colors["CYAN"] + "Ta ett fordon och kör iväg!!!"),
                "exe": self.körIväg
            },

            6: {
                "text": (styles.Colors["GREEN"] + "Ta en cykel och cykla iväg!!!"),
                "exe": self.taCykel
            },

            7: {
                "text": (styles.Colors["WARNING"] + "Svep in dig i en strandhandduk"),
                "exe": self.användHanduken
            },

            8: {
                "text": (styles.Colors["BLUE"] + "KATTER!!!, Rädda dem..."),
                "exe": self.katter
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
    t = tsunami(player)
    options_lista = t.kanGöra_skaparLista()


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
    except Exception as e:
        print(str(e))

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
