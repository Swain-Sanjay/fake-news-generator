# 1- import the random module
import random
# 2- create subjects
subjects = [
    "Shahrukh khan",
    "Ms Dhoni",
    "Aditya Nath",
    "Pussy Cat",
    "Car driver from Delhi",
    "A Group of Cows",
    "Prime Minister Modi"
]

actions = [
    "lunches",
    "cancels",
    "dance with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",     
]

places_of_things = [
    "at Red Fort",
    "in Mumbai Local Trains",
    "a plate of samosa",
    "inside pariament",
    "at Ganga Ghat",
    "during IPL Match",
    "at india Gate",
]

# 3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_of_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing} "
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

#print goodbye message
print("\nThanks for using the Fake News Headline Generator. have a fun day")