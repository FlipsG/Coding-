mein_dictionary = {
    'Name': 'Max',
    'Alter': 25,
    'Stadt': 'Berlin',
    'Beruf': 'Programmierer'
}

while True:
    print("\n1. Informationen anzeigen")
    print("2. Informationen aktualisieren/hinzufügen")
    print("3. Nach Schlüsselwort suchen")
    print("4. Beenden")

    auswahl = input("Bitte wählen Sie eine Option (1-4): ")

    if auswahl == '1':
        for key, value in mein_dictionary.items():
            print(f"{key}: {value}")
    elif auswahl == '2':
        key = input("Geben Sie den Schlüssel ein: ")
        value = input("Geben Sie den Wert ein: ")
        mein_dictionary[key] = value
        print(f"{key} wurde aktualisiert/hinzugefügt.")
    elif auswahl == '3':
        suchbegriff = input("Geben Sie das Schlüsselwort ein: ")
        ergebnisse = [(key, value) for key, value in
        mein_dictionary.items() if suchbegriff.lower() in 
        str(value).lower() or suchbegriff.lower() in key.lower()]
        print(f"\nErgebnisse für die Suche nach '{suchbegriff}':")
        for key, value in ergebnisse:
            print(f"{key}: {value}")
    elif auswahl == '4':
        print("Programm wird beendet.")
        break
    else:
        print("Ungültige Auswahl. Bitte geben Sie eine Zahl zwischen 1 und 4 ein.")