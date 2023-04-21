"""
Här är grunden till mitt spel
"""
import styles, os
from Assets.world import worldEvents
from Assets.player import player



# Extras:
player = player.Player(health=3, inventory_capasity=5)



# Start:
run = True
while run:
    # Tar bort allt rubble på skärmen
    os.system("cls")

    """ Update i player körs här """
    player.Update()

    """ Kör randomEvents() för att det ska hända något random i världen """
    styles.loadLineDSE(sleep=0.01, text="Världen Förändras:")

    worldEvents.randomEvent(player)
