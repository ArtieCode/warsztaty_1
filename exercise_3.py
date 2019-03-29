def zgadywanka():
    print("Pomyśl liczbę 1-1000 a ja zgadną ją w max. 10 prób")
    zgadywanka.z_min = 1
    zgadywanka.z_max = 1000


    def za_duzo():
        zgadywanka.z_max = zgadywanka.guess

    def za_malo():
        zgadywanka.z_min = zgadywanka.guess

    def zgadlem():
        print("Wygrałem!")

    def selector(question):
        while True:
            result = input(f"{question} Y/N: ")
            if result in ("y", "n", "Y", "N"):
                return True if result in ("y", "Y") else False

    while True:
        zgadywanka.guess = int((zgadywanka.z_max - zgadywanka.z_min)/2) + zgadywanka.z_min
        print(f"Zgaduję...  {zgadywanka.guess}")

        if selector("Zgadłem?"):
            zgadlem()
            break

        if selector("Za dużo?"):
            za_duzo()
            continue

        if selector("Za mało?"):
            za_malo()
            continue

        print("Nie oszukuj!")
        continue


zgadywanka()




