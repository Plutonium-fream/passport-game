import random
import info


def welcome_screen():
    print("Welcome to this simple game!")
    print("Its based of the game Papers Please")
    print("Make sure to check it out, its really good")
    print("\n You have to check if the information they say is correct.")
    print("You can do that by comparing the information in the passport to the answers they give!")
    print("Make no mistakes!")


welcome_screen()

print("")
print("Its 9 AM 14.4.2005")
mistakes = 0
people_left = 10
while people_left > 0:
    people_left = people_left - 1
    fullname = random.choice(info.names) + " " + random.choice(info.surnames)
    destanation = random.choice(info.destenations)
    print("YOU: Hello, What is your full name?")
    print(f"PERSON: {fullname}")
    print("YOU: Destenation?")
    print(f"PERSON: {destanation} ")
    print("YOU: Can i see your passport?")
    print("PERSON: Here you go!")
    legit1 = random.randint(1, 2)
    if legit1 == 1:
        passurname = fullname
    elif legit1 == 2:
        passurname = random.choice(info.surnames) + ", " + random.choice(info.names)

    legit2 = random.randint(1, 2)
    if legit2 == 1:
        expiration = random.randint(2006, 2010)
    else:
        expiration = random.randint(2001, 2004)

    print(f"FULL NAME: {passurname}")
    print(f"PASSPORT EXPIRATION YEAR: {expiration}")
    print("NLD>>>>>>>>>>>40583AH>>>>>>>>>>>>>>>>>>")
    correct = input("Can this person pass? (Y/N)").upper()
    if correct == "Y":
        if legit1 and legit2 == 1:
            print("Everything looks good! This person was allowed to pass.")
        else:
            print("WARNING: This person was not allowed to pass!")
            mistakes = mistakes + 1
    if correct == "N":
        if legit1 and legit2 == 1:
            print("This person was clear for entry!")
            mistakes = mistakes + 1
        else:
            print("Thats right, his documents where not correct")
print(f"You made {mistakes} mistake(s)")
input("Press enter to exit...")
