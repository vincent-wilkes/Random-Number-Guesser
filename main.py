import random

def guess_number():
    return int(input("Errate die Zahl zwischen 0 und 100: "))

#Eine Zufalls-Zahl wird generiert
randomnumber = random.randint(0, 100)
#Die Anzahl der Versuche wird gezählt um ggf. diese zu printen
amount_of_guesses = 1

while True:
    guess = guess_number()

    if guess > 100:
        print("Die gegeben Zahl ist zu groß! Versuchen sie es mit einer Zahl zwischen 0 und 100")
    elif guess < 0:
        print("Die gegeben Zahl ist zu klein! Versuchen sie es mit einer Zahl zwischen 0 und 100")
        continue

    if guess == randomnumber:
        print("Du hast die Zahl korrekt erraten")
        break
    elif abs(guess-randomnumber) <= 5:
        #Die Anzahl der Versuche wird um eins hochgesetzt
        amount_of_guesses = amount_of_guesses + 1
        print(f"Knapp daneben ist auch vorbei, du bekommst aber einen {amount_of_guesses}. Versuch! Die Zahl war: {randomnumber}")
    else:
        print(f"Das ist falsch, die Zahl war {randomnumber}")
        break
