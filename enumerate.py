

def main():
    fruit=["appel","peer","benaan","sinaasappel"]
    while True:
        print("1. door loop een lijst")
        print("2. voeg fruit toe")
        print("3. verwijder fruit uit de lijst")
        print("q stop het programma")
        keuze=input("geef je keuze in: ")
        match keuze:
            case "1":
                for index, elem in enumerate(fruit):
                    print(index, elem)
            case "2":
                nieuw_fruit=input("geef meer ")
                fruit.append(nieuw_fruit)
            case "3":
                verwijder_fruit = input("verwijderen: ")
                try:
                    fruit.remove(verwijder_fruit)
                    print(f"{verwijder_fruit} is verwijderd")
                except ValueError:
                    print(f"{verwijder_fruit} niet gevonden")
            case "q":
                break
            case _ :
                print("ongeldige input")

def enumerate(fruit, start=0):
    n = start
    for elem in fruit:
        yield n, elem
        n += 1

if __name__=="__main__":
    main()