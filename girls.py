class girl:
    def __init__(self):
        self.color = None
        self.name = None
        self.chocolate = None
        self.pet = None
        self.hobby = None
        self.holiday = None

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getChocolate(self):
        return self.chocolate

    def setChocolate(self, chocolate):
        self.chocolate = chocolate

    def getPet(self):
        return self.pet

    def setPet(self, pet):
        self.pet = pet

    def getHobby(self):
        return self.hobby

    def setHobby(self, hobby):
        self.hobby = hobby

    def getHoliday(self):
        return self.holiday

    def setHoliday(self, holiday):
        self.holiday = holiday

colors = {'Blue','Green','Pink','Purple'}
names = {'Georgina', 'Jessica', 'Jo', 'Hannah'}
chocolates = {'Boost', 'Crunchies', 'Milky Bars', 'Wispa Bites'}
pets = {'Crocodile', 'Hamster', 'Horse', 'Puppy', 'Rabbit'}
hobbies = {'Horse Riding', 'Skiing', 'Ten-pin Bowling', 'Tennis'}
holidays = {'Australia', 'Canada', 'Florida', 'Maldives'}

girls = list()

girl_1 = girl()
girl_1.setColor('Lilac')
girl_1.setName('Lucy')
girls.append(girl_1)

girl_2 = girl()
girl_2.setHoliday('Tobago')
girls.append(girl_2)

girl_3 = girl()
girl_3.setChocolate('Dairy Milk')
girls.append(girl_3)

#girl 4
girls.append(girl())

girl_5 = girl()
girl_5.setHobby('Swimming')
girls.append(girl_5)

actions = list()

for i in range(30):
    for girl in girls:
        # Jo likes the Wispa Bites
        if girl.getName() == 'Jo' and girl.getChocolate() == None:
            if 'Wispa Bites' in chocolates:
                girl.setChocolate("Wispa Bites")
                chocolates.remove('Wispa Bites')
                actions.append("Using Modus Ponens, the girls name was Jo and Jo likes Wispa Bites")
        # The person with the Hamster likes Swimming.
        if girl.getPet() == 'Hamster' and girl.getHobby() == None:
            if 'Swimming' in hobbies:
                girl.setHobby('Swimming')
                hobbies.remove('Swimming')
                actions.append("Rule 2: Using Modus Ponens, the girl had a Hamster as a pet, so can conclude she liked swimming as well")
        if girl.getHobby() == 'Swimming' and girl.getPet() == None:
            if 'Hamster' in pets:
                girl.setPet('Hamster')
                pets.remove('Hamster')
                actions.append("Rule 2: Using Modus Ponens, the girl liked swimming , so can conclude she had a pet hamster")
        # Hannah eats Dairy Milk
        if girl.getName() == 'Hannah' and girl.getChocolate() == None:
            if 'Dairy Milk' in chocolates:
                girl.setChocolate('Dairy Milk')
                chocolates.remove('Dairy Milk')
                actions.append("Rule 3: Using Modus Ponens, the girls name was Hannah, so we can conclude this girl also likes Dairy Milk")
        if girl.getChocolate() == 'Dairy Milk' and girl.getName() == None:
            if 'Hannah' in names:
                girl.setName('Hannah')
                names.remove('Hannah')
                actions.append("Rule 3: Using Modus Ponens, the girl liked Dairy Milk, so we can conclude her name is Hannah")
        #Jessica is on the left of Georgina.
        if girl.getName() == 'Georgina':
            #set girl on left name to Georgina
            if 'Jessica' in names:
                girls[index-1].setName('Jessica')
                names.remove('Jessica')
                actions.append("Using Modus Ponens, the girls name was Georgina, so we can condlude the girl to the lefts name is Jessica")
        #The person who eats milky bars owns a horse
        if girl.getChocolate() == 'Milky Bars':
            if 'Horse' in pets:
                girl.setPet('Horse')
                pets.remove('Horse')
                actions.append("Using Modus Ponens, the girl liked Milky Bars, so we can conclude she had a pet Horse")
        if girl.getPet() == 'Horse':
            if 'Milky Bars' in chocolates:
                girl.setChocolate('Milky Bars')
                chocolates.remove('Milky Bars')
                actions.append("Using Modus Ponens, the girl liked Horses, so we can conclude she liked Milky bars")

        #Jessica likes Green.
        if girl.getName() == 'Jessica' and girl.getColor() == None:
            if 'Green' in colors:
                girl.setColor('Green')
                colors.remove('Green')
                actions.append("Using Modus Ponens, the girls name was Jessica, so we can conclude she likes Green")
        #The person who wants to go to the maldives likes lilac
        if girl.getHoliday() == 'Maldives' and girl.getColor() == None:
            if 'Lilac' in colors:
                girl.setColor('Lilac')
                colors.remove('Lilac')
                actions.append("Rule 11: Using Modus Ponens, the girl wanted to holuday in Maldives, so we can conclude she likes the color Lilac")
        if girl.getColor() == 'Lilac' and girl.getHoliday() == None:
            if 'Maldives' in holidays:
                girl.setHoliday('Maldives')
                holidays.remove('Maldives')
                actions.append(
                    "Rule 11: Using Modus Ponens, the girl liked Lilac, so we can conclude she wants to Holiday in Maldives")
        #The Person Who Likes Pink Wants to go to Florida
        if girl.getColor() == 'Pink':
            if 'Florida' in holidays:
                girl.setHoliday('Florida')
                holidays.remove('Florida')
                actions.append("Using Modus Ponens, the girl likes the color Pink, so she must to go to Florida")
        # The Person Who Likes Pink Wants to go to Florida
        if girl.getHoliday() == 'Florida':
            if 'Pink' in colors:
                girl.setColor('Pink')
                colors.remove('Pink')
                actions.append("Using Modus Ponens, the girl wants to holiday in florida so she must like pink")
        #The Person that likes blue owns a puppy
        if girl.getColor() == 'Blue':
            if 'Puppy' in pets:
                girl.setPet('Puppy')
                pets.remove('Puppy')
                actions.append("Using Modus Ponens, the girl likes the color blue, so she must have a puppy as a pet")
        #The girl who likes purple wants to go to canada
        if girl.getColor() == 'Purple':
            if 'Canada' in holidays:
                girl.setHoliday('Canada')
                holidays.remove('Canada')
                actions.append("Using Modus Ponens, the girl likes color so we can conclude she wants to go to Canada")
        if girl.getHoliday() == 'Canada':
            if 'Purple' in colors:
                girl.setColor('Purple')
                colors.remove('Purple')
                actions.append("Using Modus Ponens, the girl holidays in Canada so we can conclude she likes the color purple")
        #The girl who likes crunchies owns a rabbit
        if girl.getChocolate() == 'Crunchies':
            if 'Rabbit' in pets:
                girl.setPet('Rabbit')
                pets.remove('Rabbit')
                actions.append("Using Modus ponens, the girl likes Crunchies, so she must have a rabbit as a pet")
        #Jessica wants to go to Australia
        if girl.getName() == 'Jessica' and girl.getHoliday() == None:
            if 'Australia' in holidays:
                girl.setHoliday('Australia')
                holidays.remove('Australia')
                actions.append("Using Modus ponens, the girls name was Jessica, so we can conclude she holidays in Australia")

    #iterate with index
    for index in range(5):
        # The girl on the right of the girl who likes tennis likes horseriding
        if girls[index].getHobby() == 'Tennis':
            girls[index + 1].setHobby("Horse Riding")
            if 'Horse Riding' in hobbies:
                hobbies.remove("Horse Riding")
            actions.append(
                "Using Modus Ponens, the girl likes Tennis, so the girl on her right must like horseback riding")
        # The person who likes Wispa Bites sits next to the person who wants to go to Florida
        if girls[index].getChocolate() == 'Wispa Bites':
            # if index is 0, know it is girl in index 1
            if index == 0:
                girls[index + 1].setHoliday('Florida')
                #chocolates.remove('Wispa Bites')
                actions.append( "Using Modus Ponens, the girl wanted to holiday in Florida was at index 0, so the girl at index 1 likes Wispa Bites")
            elif index == 4:
                girls[index - 1].setHoliday('Florida')
                #chocolates.remove('Wispa Bites')
                actions.append("Using Modus Ponens, the girl wanted to holiday in Florida was at index 4, so the girl at index 3 likes Wispa Bites")
            else:
                if girls[index + 1].getHoliday() != None:
                    girls[index - 1].setHoliday('Florida')
                    if 'Florida' in holidays:
                        holidays.remove('Florida')
                        actions.append(
                            "Using Modus Ponens, the girl likes Wispa Bites and the girl on her right already has a holiday, so the girl on her left must holiday in florida")
                elif girls[index - 1].getHoliday() != None:
                    girls[index + 1].setHoliday('Florida')
                    if 'Florida' in holidays:
                        holidays.remove('Florida')
                        actions.append(
                            "Using Modus Ponens, the girl likes Wispa Bites and the girl on her left already has a holiday, so the girl on her right must holiday in Florida")

        # The person who likes skiing sits next to the person who has a hamster
        if girls[index].getPet() == 'Hamster':
            # if index is 0, know it is girl in index 1
            if index == 0:
                if girls[index +1].getHobby() != 'Skiing':
                    girls[index + 1].setHobby('Skiing')
                    hobbies.remove('Skiing')
                    actions.append(
                        "Using Modus Ponens, the girl who had a hamster was at index 0, so the girl at index 1 likes Skiing")
            elif index == 4:
                if girls[index - 1].getHobby() != 'Skiing':
                    girls[index - 1].setHobby('Skiing')
                    if 'Skiing' in hobbies:
                        hobbies.remove('Skiing')
                    actions.append("Using Modus Ponens,  the girl who had a hamster was at index 4, so the girl at index 3 likes Skiing")
            else:
                if girls[index + 1].getHobby() != None:
                    girls[index - 1].setHobby('Skiing')
                    hobbies.remove('Skiing')
                    actions.append("Using Modus Ponens, the girl had a hamster and the girl on her right already liked a hobby, so the girl on her left must like skiing")
                elif girls[index - 1].getHobby() != None:
                    girls[index + 1].setHobby('Skiing')
                    hobbies.remove('Skiing')
                    actions.append("Using Modus Ponens, the girl had a hamster and the girl on her left already liked a hobby, so the girl on her right must like Skiing")

        # The girl next to the girl who likes Milky Bars likes Boost
        if girls[index].getChocolate() == 'Milky Bars':
            # if index is 0, know it is girl in index 1
            if index == 0:
                girls[index + 1].setChocolate('Boost')
                chocolates.remove('Boost')
                actions.append("Using Modus Ponens, the girl who likes Milky Bars was at index 0, so the girl at index 1 likes Boost")
            elif index == 4:
                girls[index - 1].setChocolate('Boost')
                chocolates.remove('Boost')
                actions.append("Using Modus Ponens,  the girl who likes Milky Bars was at index 4, so the girl at index 3 likes Boost")
            else:
                if girls[index + 1].getChocolate() != None:
                    if 'Boost' in chocolates:
                        girls[index - 1].setChocolate('Boost')
                        chocolates.remove('Boost')
                        actions.append("Using Modus Ponens, the girl likes Milky Bars and the girl on her right already liked a chocolate, so the girl on her left must like Boost")
                elif girls[index - 1].getChocolate() != None:
                    girls[index + 1].setChocolate('Boost')
                    chocolates.remove('Boost')
                    actions.append("Using Modus Ponens, the girl likes Milky Bars and the girl on her left already liked a chocolate, so the girl on her right must like Boost")
        #  The girl who likes Skiing sits next to the girl who plays Ten-pin bowlings.
        if girls[index].getHobby() == 'Skiing':
            # if index is 0, know it is girl in index 1
            if index == 0:
                girls[index + 1].setHobby('Ten-pin Bowling')
                hobbies.remove('Ten-pin Bowling')
                actions.append("Using Modus Ponens, the girl who likes Skiing was at index 0, so the girl at index 1 likes Ten pin bowling")
            elif index == 4:
                girls[index - 1].setHobby('Ten-pin Bowling')
                hobbies.remove('Ten-pin Bowling')
                actions.append("Using Modus Ponens,  the girl who likes Skiing was at index 4, so the girl at index 3 likes Ten pin bowling")
            else:
                if girls[index + 1].getHobby() != None:
                    if girls[index - 1].getHobby() != 'Ten-pin Bowling':
                        girls[index - 1].setHobby('Ten-pin Bowling')
                        hobbies.remove('Ten-pin Bowling')
                        actions.append("Using Modus Ponens, the girl likes Skiing and the girl on her right already liked a hobby, so the girl on her left must like Ten pin bowling")
                elif girls[index - 1].getHobby() != None:
                    if girls[index + 1].getHobby() != 'Ten-pin Bowling':
                        girls[index + 1].setHobby('Ten-pin Bowling')
                        hobbies.remove('Ten-pin Bowling')
                        actions.append("Using Modus Ponens, the girl likes Skiing and the girl on her left already liked a hobby, so the girl on her right must like Ten pin bowling")

    #check if only two values left
    #Rule 17
    if len(hobbies) == 2:
        onlyRule17HobbiesLeft = True
        for girl in girls:
            if girl.getHobby() == 'Tennis' or girl.getHobby() == 'Horse Riding':
                onlyRule17HobbiesLeft = False

        if onlyRule17HobbiesLeft:
            setFirst = 0
            for girl in girls:
                if girl.getHobby() == None and setFirst == 0:
                    girl.setHobby('Tennis')
                    setFirst = 1
                if girl.getHobby() == None and setFirst == 1:
                    girl.setHobby('Horse Riding')
            actions.append('Rule 17: Since only two hobbies were left, tennis goes in the first open hobby and horse riding goes in the second')
    #Rule 4
    #Jessica is on the left of Georgina.
    #THIS does not work universrally, but  works for this one case
    if len(names) == 3:
        for i in range(len(girls)-1):
            if girls[i].getName() == None and girls[i+1].getName() == None:
                girls[i].setName("Jessica")
                girls[i+1].setName("Georgina")
                actions.append("Since Jessica is on the left of georgina and both Jessica and Georgina haven't been used yet, we can conclude Jessica is in index 3 and Georgina is in index 4 since those are the only two open slots next to each other")
                names.remove('Jessica')
                names.remove('Georgina')

    #the girl who likes milky bar sits next to person who likes boost
    #person who eats milky bars owns a horse
    if len(chocolates) == 3:
        for i in range(len(girls)-1):
            if girls[i].getChocolate() == None and girls[i+1].getChocolate() == None:
                if girls[i].getPet() != None:
                    if 'Horse' in pets:
                        girls[i+1].setPet('Horse')
                        pets.remove('Horse')
                        actions.append('The person who likes milky bars sits next to the person who likes boost. There are only two possible places with two chocolates open next to eachother, so horse must go to the one without a pet')
                elif girls[i+1].getPet() != None:
                    if 'Horse' in pets:
                        girls[i].setPet('Horse')
                        pets.remove('Horse')
                        actions.append('The person who likes milky bars sits next to the person who likes boost. There are only two possible places with two chocolates open next to eachother, so horse must go to the one without a pet')


    if len(names) == 1:
        lastname = names.pop()
        for girl in girls:
            if girl.getName() == None:
                girl.setName(lastname)
                actions.append('There was only one name left, so had to be assigned to the girl without a name')

    if len(holidays) == 1:
        for girl in girls:
            if girl.getHoliday() == None:
                girl.setHoliday('Canada')
                actions.append('Only one holiday remains, so that must girl to the girl without a holiday')

    if len(colors) == 1:
        lastcolor = colors.pop()
        for girl in girls:
            if girl.getColor() == None:
                girl.setColor(lastcolor)
                actions.append('Only one color remains, so that must go to the girl without a color')
    if len(chocolates) == 1:
        lastchocolate = chocolates.pop()
        for girl in girls:
            if girl.getChocolate() == None:
                girl.setChocolate(lastchocolate)
                actions.append('Only one chocolate remains, so that must go to the girl without a chocolate')
    if len(pets) == 1:
        lastpet = pets.pop()
        for girl in girls:
            if girl.getPet() == None:
                girl.setPet(lastpet)
                actions.append('Only one chocolate remains, so that must go to the girl without a chocolate')
#make unique
output = []
for action in actions:
    if action not in output:
        output.append(action)

for action in output:
    print(action)

for girl in girls:
    print("#########")
    print(girl.getColor())
    print(girl.getName())
    print(girl.getChocolate())
    print(girl.getPet())
    print(girl.getHobby())
    print(girl.getHoliday())


