

def ask_for_the_age(name):
    age_int = -1
    while age_int == -1:
        age_str = input(name + ", what is your age? ")
        try:
            age_int = int(age_str)
        except:
            print("Error: Age must be a number")
    return age_int


def ask_for_the_height():
    height_float = 0
    height_str = input(name + ", How tall are you in meters? ")
    try:
        height_float = float(height_str)
    except:
        print("Error: height must be a number")
    return height_float


def ask_for_the_name():
    name_answer = ""
    while name_answer == "":
        name_answer = input("What is your name? ")
    return name_answer


def display_input(name, age, height):
    print()
    print(f"Your name is {name}. You are {age} years old.")
    print(f"Soon you will be {age + 1}.")
    if age == 17:
        print("You are almost an adult.")
    elif 10 <= age < 18:
        print("You are a teenager.")
    elif age == 18:
        print("You are now an adult. Congratz!!")
    elif age > 60:
        print("You are a senior")
    elif age >= 18:
        print("You are a adult.")
    elif age == 1 or age == 2:
        print("You are a baby")
    elif age < 10:
        print("You are a kid.")
    else:
        print("You are a minor.")
    if not height == 0:
        print(f"Your height: {height}m")

group_size = 0
group_size_input = input("How many people in your party?")
try:
    group_size = int(group_size_input)
except:
    print("Error: Your party must be a number")
for i in range(0, group_size):
    name = ask_for_the_name()
    age = ask_for_the_age(name)
    height = ask_for_the_height()
    display_input(name, age, height)

