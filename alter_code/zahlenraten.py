import random

def zahlenraten():
    print("Willkommen beim Zahlenraten-Spiel!")
    zielzahl = random.randint(1, 20)  # Zufällige Zahl zwischen 1 und 20 generieren
    versuche = 0

    while True:
        guess = int(input("Rate eine Zahl zwischen 1 und 20: "))
        versuche += 1

        if guess < zielzahl:
            print("Zu niedrig! Versuche es erneut.")
        elif guess > zielzahl:
            print("Zu hoch! Versuche es erneut.")
        else:
            print(f"Glückwunsch! Du hast die Zahl {zielzahl} erraten.")
            print(f"Du hast {versuche} Versuche gebraucht.")
            break

zahlenraten()
