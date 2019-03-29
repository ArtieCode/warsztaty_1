import random


def lotto():

    class OutOfLottoRangeException(Exception):
        """Użyć jeśli wprowadzana liczba nie jest z zakresu 1-49"""

    class LottoRepetitionException(Exception):
        """Użyć jeśli wprowadzana liczba jest już w zestawie"""

    def initialise():
        print("\n" + "LOTTO" + "\n" + "Wprowadź kolejno 6 liczb z zakresu 1-49" + "\n" + "Aby przerwać działanie programu wprowadź 'q'")
        lotto.numbers = []
        lotto.lucky = 0
        lotto.secret = random.sample(range(1, 50), 6)
        lotto.secret.sort()
        lotto.user_quit = False

    def main_loop():
        while len(lotto.numbers) != 6:
            try:
                user_input = input("Wprowadź liczbę: ")

                if user_input == 'q':
                    lotto.user_quit = True
                    break

                input_attempt = int(user_input)

                if input_attempt in lotto.numbers:
                    raise LottoRepetitionException

                if input_attempt not in range(1, 50):
                    raise OutOfLottoRangeException

                lotto.numbers.append(input_attempt)
                continue

            except ValueError:
                print("To nie jest liczba naturalna, spróbuj ponownie: ")
                continue

            except OutOfLottoRangeException:
                print("Liczba wykracza poza zakres 1-49, spróbuj ponownie: ")
                continue

            except LottoRepetitionException:
                print("Ta liczba jest już w Twoim zestawie, wybierz inną: ")
                continue


    def results():
        lotto.numbers.sort()

        for number in lotto.numbers:
            if number in lotto.secret:
                lotto.lucky += 1
        if not lotto.user_quit:
            print(f"Twoje liczby to: {lotto.numbers}, zwycięskie liczby to: {lotto.secret}, Trafiłeś {lotto.lucky}")
            initialise()
            main_loop()

    initialise()
    main_loop()
    results()



lotto()
