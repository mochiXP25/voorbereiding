from pathlib import Path

def zoek_bestanden(path):
    path = Path(path)

    if path.is_dir():
        print("deze map heeft volgende bestanden:")
        bestanden = list(path.glob('*.py'))
        if bestanden:
            for bestand in bestanden:
                print(bestand.name)
        else:
            print("Geen Python bestanden")
    else:
        print("Dit is geen map.")

if __name__ == "__main__":
    path = input("Welke map moet ik doorzoeken? ")
    zoek_bestanden(path)
