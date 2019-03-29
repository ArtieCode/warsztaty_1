import random

def zgadywanka():

    def initialise():
        print("ZGADYWANKA" + "\n" + "Zgadnij liczbę naturalną 1-100!" + "\n" + "Aby przerwać działanie programu wprowadź 'q'")
        zgadywanka.number = 0
        zgadywanka.secret = random.randint(1, 100)

    initialise()

    while True :
        try:
            user_input = input("Wprowadź liczbę: ")
            if user_input == 'q':
                break
            zgadywanka.number = int(user_input)
        except ValueError:
            print("To nie jest liczba naturalna z zakresu 1 - 100")
            continue
        if zgadywanka.number != zgadywanka.secret:
            print(("Za mało!", "Za dużo!")[zgadywanka.number > zgadywanka.secret])
        else:
            print("Zgadłeś!" + "\n")
            initialise()


zgadywanka()
