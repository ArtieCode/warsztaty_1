def zgadywanka():
    print("Pomyśl liczbę 1-1000 a ja zgadną ją w max. 10 prób")
    min = 1
    max = 1000

    def za_duzo():
        zgadywanka.max = guess

    def za_malo():
        zgadywanka.min = guess

    def zgadlem():
        print("Wygrałem!")

    while True:
        guess = int((max-min)/2) + 1
        print(f"Zgaduję...  + {guess}")
        guessed = input("Zgadłem? y/n: ")

        if guessed == "y":
            zgadlem()
            break
        too_much = input("Za dużo? y/n: ")

        if too_much == "y":
            za_duzo()
            continue
        if






