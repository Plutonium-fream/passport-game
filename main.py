import random
import time
import threading

names = [
    "Aaron", "Abigail", "Adam", "Adrian", "Aiden",
    "Alexa", "Alice", "Alyssa", "Amanda", "Amber",
    "Andrew", "Angela", "Anna", "Anthony", "Ashley",
    "Ava", "Benjamin", "Blake", "Brandon", "Brian",
    "Brittany", "Caleb", "Cameron", "Caroline", "Catherine",
    "Charles", "Charlotte", "Chloe", "Christopher", "Claire",
    "Daniel", "David", "Dylan", "Ella", "Emily",
    "Emma", "Ethan", "Evan", "Gabriel", "Grace",
    "Hannah", "Isabella", "Jacob", "James", "John",
    "Jonathan", "Jordan", "Joseph", "Joshua", "Kaitlyn",
    "Katherine", "Kayla", "Kevin", "Kimberly", "Kyle",
    "Laura", "Lauren", "Layla", "Liam", "Lillian",
    "Lily", "Logan", "Lucas", "Lucy", "Madeline",
    "Madison", "Maria", "Mason", "Matthew", "Megan",
    "Michael", "Mia", "Michelle", "Molly", "Nathan",
    "Nicholas", "Noah", "Olivia", "Owen", "Patrick",
    "Rachel", "Rebecca", "Ryan", "Samantha", "Samuel",
    "Sarah", "Savannah", "Scarlett", "Sean", "Sophia",
    "Sophie", "Stephen", "Taylor", "Thomas", "Tyler",
    "Victoria", "William", "Zachary", "Zoe", "Zach"
]
surnames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris",
    "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright",
    "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall",
    "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz",
    "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook",
    "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
    "Peterson", "Bailey", "Reed", "Kelly", "Howard",
    "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James",
    "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
    "Price", "Alvarez", "Castillo", "Sanders", "Patel",
    "Myers", "Long", "Ross", "Foster", "Jimenez"
]
destenations = [
    "Astronville", "Bladeport", "Crescent Hollow", "Dragonspire", "Eagle's Rest",
    "Frostford", "Glitterfall", "Havenwood", "Ironcliff", "Jadewater",
    "Kingsreach", "Luminara", "Mystvale", "Nimbus City", "Oakshade",
    "Pyrestone", "Quartz Harbor", "Ravenbrook", "Silverpeak", "Thornfield"
]
countries = [
    "Zephyrosia",
    "Luminara",
    "Aqualis",
    "Drakoria",
    "Solvatria",
    "Virelia",
    "Cyranthia"
]


def welcome_screen():
    print("Welcome to this simple game!")
    print("Its based of the game Papers Please")
    print("Make sure to check it out, its really good")
    print("\nYou have to check if the information they say is correct. And follow the extra conditions that you will "
          "hear at the start")
    print("You can do that by comparing the information in the passport to the answers they give!")
    print("You have to check as many people as possible in one minute.")
    print("Try to make no mistakes.")
    print("Good luck!")


welcome_screen()


class Scenerio:
    def __init__(self, description, name, code):
        description = description
        name = name
        code = code


virus_spread = Scenerio("Dont let people from Drakoria in, their country has a deadly virus", "Drakorian Virus", 1)


def background_timer(seconds):
    global timeleft
    timeleft = seconds
    while seconds > 0:
        time.sleep(1)
        timeleft = timeleft - 1


def start_timer(seconds):
    timer_thread = threading.Thread(target=background_timer, args=(seconds,))
    timer_thread.daemon = True
    timer_thread.start()


print("Its 9 AM 14.4.2005")
mistakes = 0
people = 0
input("Press enter to begin!  ")
print("")
print("")
start_timer(60)
while timeleft > 0:
    print(f"You have {timeleft} seconds left")
    people += 1
    residence = random.choice(countries)
    fullname = random.choice(names) + " " + random.choice(surnames)
    destanation = random.choice(destenations)
    print("YOU: Hello, What is your full name?")
    print(f"PERSON: {fullname}")
    print("YOU: Destenation?")
    print(f"PERSON: {destanation} ")
    print("YOU: Can i see your passport?")
    print("PERSON: Here you go!")
    print("")
    legit1 = random.randint(1, 2)
    if legit1 == 1:
        passurname = fullname
    elif legit1 == 2:
        passurname = random.choice(surnames) + ", " + random.choice(names)

    legit2 = random.randint(1, 2)
    if legit2 == 1:
        expiration = random.randint(2006, 2010)
    else:
        expiration = random.randint(2001, 2004)
    print(f"Citizen of the country of {residence}")
    print(f"FULL NAME: {passurname}")
    print(f"PASSPORT EXPIRATION YEAR: {expiration}")
    print("LSL>>>>>>>>>>>40583AH>>>>>>>>>>>>>>>>>>")
    print("")
    correct = input("Can this person pass? (Y/N)").upper()
    if correct == "Y":
        if legit1 == 1 and legit2 == 1:
            print("Everything looks good! This person was allowed to pass.")
        else:
            print("WARNING: This person was not allowed to pass!")
            mistakes = mistakes + 1
    if correct == "N":
        if legit1 == 1 and legit2 == 1:
            print("This person was clear for entry!")
            mistakes = mistakes + 1
        else:
            print("Thats right, his documents where not correct")
if mistakes == 0:
    print("Wow, No mistakes! You are promoted!")
else:
    print(f"You made {mistakes} mistake(s)")
    input("Press enter to exit...")
