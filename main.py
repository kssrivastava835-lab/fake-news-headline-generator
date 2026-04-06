import random

subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmal Sitharaman",
    "A Mumbai cat",
    "A Group of monkeys",
    "Prime Minister Modi",
    "Auto Rikshaw Driver from Delhi",
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at red fort",
    "in Mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ghat",
    "during IPL Match",
    "at India Gate",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip()
    if user_input == "no":
        break

print("\nThanks for using the Fake News Headline Generator.")