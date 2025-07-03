import random

guess = int(input("Errate die Zahl zwischen 0 und 100: "))
randomnumber = random.randint(0, 100)

if guess == randomnumber:
    print("Du hast die Zahl korrekt erraten")
elif guess > 100:
    print("Die gegeben Zahl ist zu groß! Versuchen sie es mit einer Zahl zwischen 0 und 100")
elif guess < 0:
    print("Die gegeben Zahl ist zu klein! Versuchen sie es mit einer Zahl zwischen 0 und 100")
elif abs(guess-randomnumber) == 5:
    print(f"Knapp daneben ist auch vorbei: die Zahl ist {randomnumber}")
else:
    print(f"Das ist falsch, die Zahl ist {randomnumber}")
