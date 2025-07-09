import random

user_input = input("Gib den Zahlenbereich als zwei Zahlen ein, z.B. '10,50' oder '10:50': ")

#Jetzt wird der User Input mit gängigen Seperatoren aufgeteilt und dann in eine sortierte Liste aus Integern gestellt
for Sep in [',', ';', ':', '-', '.', ' ', '/']:
    if Sep in user_input:
        numberrange = sorted(map(int, user_input.split(Sep)))
        break
else:
    raise ValueError("Bitte gibt zwei Zahlen mit einem Trennzeichen wie ',' oder ':' ein.")

rangesize = abs(numberrange[0] - numberrange[1])

if rangesize <= 20:
    raise ValueError("Das ist ein wenig zu einfach, versuche es mit einem Zahlenraum der größer als 20 ist.")

#Eine Zufalls-Zahl wird generiert
randomnumber = random.randint( numberrange[0], numberrange[1])
amount_of_guesses = 1
relative_accuracy = rangesize / 20

while True:
    guess = int(input(f"Errate die Zahl zwischen {numberrange[0]} und {numberrange[1]}: "))

    if guess < numberrange[0]:
        raise ValueError(f"Die gegebene Zahl ist zu klein! Versuche es mit einer Zahl zwischen {numberrange[0]} und {numberrange[1]}.")
    elif guess > numberrange[1]:
        raise ValueError(f"Die gegebene Zahl ist zu groß! Versuche es mit einer Zahl zwischen {numberrange[0]} und {numberrange[1]}.")

    if guess == randomnumber:
        print("Herzliche Glückwunsch, du hast die Zahl korrekt erraten!")
        break
    elif abs(guess-randomnumber) <= relative_accuracy:
        #Die Anzahl der Versuche wird um eins hochgesetzt
        amount_of_guesses = amount_of_guesses + 1
        print(f"Knapp daneben ist auch vorbei, du bekommst aber einen {amount_of_guesses}. Versuch!")
    else:
        print(f"Das ist falsch, die Zahl war {randomnumber}.")
        break
