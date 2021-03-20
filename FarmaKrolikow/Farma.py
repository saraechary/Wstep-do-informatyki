import random


class Rabbit():
    def __init__(self, race, age, maxage, spozjedzenia, isfed, wsprozrodczy, cenazakupu, cenasprzed):
        self.race = race
        self.age = 0
        self.maxage = maxage
        self.spozjedzenia = spozjedzenia
        self.isfed = isfed
        self.wsprozrodczy = wsprozrodczy
        self.cenazakupu = 300+50*(self.maxage - 12)+100*(self.wsprozrodczy-2)
        self.cenasprzed = cenasprzed

    def isAlive(self):
        if self.isfed and self.age<self.maxage:
            return 1
        return 0

    def feed(self):
        self.isfed = 1
        return self.spozjedzenia

    def sell(self):
        return self.cenasprzed 

    def buy(self):
        return self.cenazakupu

    def ageing(self):
        self.age += 1

    def __add__(self, partner):
        return (self.wsprozrodczy+partner.wsprozrodczy)//2

    def __repr__(self):
        return "Rasa: %s, Wiek: %s, Wartość: %s" %(self.race,self.age,self.cenasprzed)


class GoldenRabbit(Rabbit):
    lastbuff = 0

    def __init__(self):
        super().__init__("Golden Rabbit", 0, 12, 1, 1, 3, None, 400)
        self.cenazakupu = 600
        self.psvincome = random.randint(100, 200)

    def buff(self, currmonth):
        if currmonth - GoldenRabbit.lastbuff >= 3:
            GoldenRabbit.lastbuff = currmonth
            print("Golden rabbit jest gotów spełnić Twoje 1 życzenie!\nCo wybierasz?")
            print("1 - wszystkie króliki zostają nakarmione w tej turze(ilość jedzenia pozostaje niezmieniona)\n"
                  "2 - otrzymujesz dodatkowe 200 golda\n"
                  "3 - w tej turze króliki się nie rozmnażają")
            choice = input("Twój wybór: ")  # walidacja inputa do zrobienia
            return choice
        return 0


class Farm():
    def __init__(self, cash, food, species ,rabbits, maxrabbits):
        self.cash = cash
        self.food = food
        self.species = species
        self.rabbits = rabbits
        self.maxrabbits = maxrabbits
        self.months = 0

    def buyFood(self,amount):
        if 10*amount>self.cash:
            print ("Za mało pieniędzy")
        else:
            self.food += amount
            self.cash -= 10*amount
        print ("Kupiono %i jedzenia za %i pieniędzy" %(amount,10*amount))

    def feedRabbits(self):
        fed = self.food
        for i in range (self.food):
            self.rabbits[i].feed()
            self.food -= 1

        if fed < len(self.rabbits):
            for r in self.rabbits[fed:]:
                r.isfed = 0

    def buyRabbit(self,quality):
        if quality == 1:
            if self.cash>=300:
                r = Rabbit(None,0,12,1,3,None,None, None)
                self.rabbits.append(r)
                self.cash -= 300
            else:
                print ("Za mało pieniędzy na kupno tego królika")

        elif quality == 2:
            if self.cash>=400:
                r = Rabbit(None,0,13,1,5,None,None, None)
                self.rabbits.append(r)
                self.cash -= 400
            else:
                print ("Za mało pieniędzy na kupno tego królika")

        elif quality == 3:
            if self.cash>=500:
                r = Rabbit(None,0,14,1,5,None,None, None)
                self.rabbits.append(r)
                self.cash -= 500
            else:
                print ("Za mało pieniędzy na kupno tego królika")

    def sellRabbit(self):
        pass

    def deleteRabbit(self):
        for r in self.rabbits:
            if not r.isAlive():
                self.rabbits.remove(r)

    def reproduce(self):
        newGen = 0

        for i in range(0, len(self.rabbits), 2):
            if i+1 < len(self.rabbits):
                newGen += (self.rabbits[i] + self.rabbits[i+1])

        for i in range(newGen):
            r = Rabbit(None, 0, random.randint(12, 14), 1, 1, random.randint(3, 5), None, None)
            self.rabbits.append(r)

    def ismaxCapacity(self):
        if len(self.rabbits) > self.maxrabbits:
            print("Doszło do przepełnienia farmy.\nUciśnione króliki dokonały rewolty i z niej uciekły.\nKoniec gry :(")
            return 1
        return 0

    def __repr__(self):
        return "Stan farmy {}. miesiąc:\nIlość królików: {}/{}\tIlość pieniędzy: {}\tIlość jedzenia: {}".format(self.months, len(self.rabbits), self.maxrabbits, self.cash, self.food)



