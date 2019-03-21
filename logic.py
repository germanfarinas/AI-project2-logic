from kanren import *


def right_of(p, q, l):
    return membero((q, p), zip(l, l[1:]))

def next_to(p, q, l):
    return conde([right_of(p, q, l)], [right_of(q, p, l)])

"""Five girls are sitting in a row. Each girl has a favorite color, 
a chocolate bar, a pet, a hobby, and a place to go on holiday. 
Determine the name of the girl who owns the crocodile."""

girls = var()
constraints = lall(
    # There are five girls
    (eq, (var(), var(), var(), var(), var()), girls),
    #  Jo likes the Wispa Bites.
    #  color name chocolate pet hobby holiday
    (membero, (var(), "Jo", "Wispa Bites", var(), var(), var()), girls),
    #  Hannah eats Dairy Milk.
    (membero, (var(), "Hannah", "Dairy Milk", var(), var(), var()), girls),
    #  The person with the Hamster likes Swimming.
    (membero, (var(), var(), var(), "Hamster", "Swimming", var()), girls),
    #  Jessica is on the left of Georgina.
    (right_of, (var(), "Jessica", var(), var(), var(), var()), (var(), "Georgina"), var(), var(), var(), var()),
    #  Lucy is the first on the left.
    (eq, ((var(), "Lucy", var(), var(), var(), var()), var(), var(), var(), var()), girls),
    #  The first person on the right likes Swimming.
    (eq, (var(), var(), var(), var(), (var(), var(), var(), var(), "Swimming", var())), girls),
    #  The person who eats Milky Bars owns a Horse.
    (membero, (var(), var(), "Milky Bars", "Horse", var(), var()), girls),
    #  The person in the middle eats Dairy Milk.
    (eq, (var(), var(), (var(), var(), "Dairy Milk", var(), var(), var()), var(), var()), girls),
    #  Jessica likes Green.
    (membero, ("Green", "Jessica", var(), var(), var(), var()), girls),
    #  The person on the left of the middle wants to go to Tobago.
    (eq, (var(), (var(), var(), var(), var(), var(), "Tobago"), var(), var(), var()), girls),
    #  The person who wants to go to the Maldives likes Lilac.
    (membero, (var(), var(), "Lilac", var(), var(), "Maldives"), girls),
    #  The person who likes Wispa Bites sits next to the person who wants to go to Florida.
    (next_to, (var(), var(), "Wispa Bites", var(), var(), var()), (var(), var(), var(), var(), var(), "Florida"), girls),
    #  The person who likes Pink wants to go to Florida.
    (membero, ("Pink", var(), var(), var(), var(), "Florida"), girls),
    #  The person who sits first on the left likes Lilac.
    (eq, ("Lilac", var(), var(), var(), var(), var()), var(), var(), var(), var(), girls),
    #  The girl that likes Blue owns a Puppy.
    (membero, ("Blue", var(), var(), "Puppy", var(), var()), girls),
    #  The person who likes Skiing sits next to the person who has a Hamster.
    (next_to, (var(), var(), var(), var(), "Skiing", var()), (var(), var(), var(), "Hamster", var(), var())),
    #  The girl on the right of the girl who likes Tennis likes Horse riding.
    (right_of, (var(), var(), var(), var(), "Tennis", var()), (var(), var(), var(), var(), "Horse riding", var()), girls),
    #  The girl next to the girl who likes Milky Bars likes Boost.
    (next_to, (var(), var(), "Milky Bars", var(), var(), var()), (var(), var(), "Boost", var(), var(), var()), girls),
    #  The girl who likes Purple wants to go to Canada.
    (membero, ("Purple", var(), var(), var(), var(), "Canada"), girls),
    #  The girl who likes Crunchies owns a Rabbit.
    (membero, (var(), var(), "Crunchies", "Rabbit", var(), var()), girls),
    #  The girl who likes Skiing sits next to the girl who plays Ten-pin bowlings.
    (next_to, (var(), var(), var(), var(), "Skiing", var()), (var(), var(), var(), var(), "Ten-pin Bowling", var()), girls),
    #  Jessica wants to go to Australia.
    (membero, (var(), "Jessica", var(), var(), var(), "Australia"), girls))

solutions = run(1, girls, constraints)
print(solutions)
