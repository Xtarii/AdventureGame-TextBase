"""
Denna script kommer att ta hand om saker i världen
alltså "World Events"

eftersom att events kommer vara random så kommer
vi att importera "random" och några andra moduler
"""
import random, styles, os
from Assets.Enemies import orch, floridaman
from Assets.world import jordbävning, tsunami





""" I event listan så finns det en text som kommer att vissas och en "exe" som kommer att köras """
# Events list:
events = {
    1: {
        "text": (styles.Colors["WARNING"] + """JORDBÄVNING!!!! Det är svårt att stå still...""" + styles.Colors["ENDC"]),

        "exe": jordbävning.kanGöras
    },

    2: {
        "text": (styles.Colors["WARNING"] + """En Orch springer emot dig, och hen är """ + styles.Colors["FAIL"] +
        "RÖD" + styles.Colors["WARNING"] + " i ansiktet, \nvad har jag gjort tänker du!!!!!" + styles.Colors["ENDC"]),

        "exe": orch.kanGöras
    },

    3: {
        "text": (styles.Colors["WARNING"] + "En stor våg närmar sig, det ser ut som en tsunami" + styles.Colors["ENDC"]),
        "exe": tsunami.kanGöras
    },

    4 : {
        "text": (styles.Colors["BLUE"] + "En florida man kommer, han springer konstigt men\n" +
        "bara för det ska man inte underskatta dem" + styles.Colors["ENDC"]),
        "exe": floridaman.kanGöras
    }
}


# Random Event generator eller start:
def randomEvent(player):
    # Gör ett random event
    eventIndex = random.randint(1, len(events))


    # Skriver ut vad eventet gör
    print(events[eventIndex]["text"])
    # En continue Delay
    input(styles.Colors["BLUE"] + "< continue >" + styles.Colors["ENDC"])
    # Kör event commandot, alltså events["exe"]
    events[eventIndex]["exe"](player)
    # Tömmer skärmen
    os.system("cls")
