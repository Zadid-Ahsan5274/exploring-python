class Animal:
    def __init__(self,birthType="Unknown",appearance="Unknown",blooded="Unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self,birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def str(self):
        print("A {} is {}. It is {} and it is {}".format(type(self).__name__, self.birthType, self.appearance, self.blooded))

class Mammal(Animal):
    def __init__(self,birthType="Born Alive",appearance="hair or fur",blooded="Warm Blooded",nurseYoung=True):
        Animal.__init__(self,birthType,appearance,blooded)
        self.nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self,nurseYoung):
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return super().__str__()+(" and it it {} they"
                                "nurse their young").format(self.nurseYoung)

class Reptile(Animal):
    def __init__(self,birthType="Born in an egg or born alive",appearance="dry scales",blooded="Cold Blooded"):
        Animal.__init__(self,birthType,appearance,blooded)

    def sumAll(self,*args):
        sum = 0
        for i in args:
            sum+=i
        return sum



def main():
    animal1 = Animal("Born Alive")
    print(animal1.birthType)
    print(animal1)

    mammal1 = Mammal()
    print(mammal1)
    print()

    reptile1 = Reptile()
    print(reptile1.birthType)
    print(reptile1)

    print("Sum : {}".format(reptile1.sumAll(1,2,3,4,5)))

    def get_birth_type(theObject):
        print("The {} is {}".format(type(theObject).__name__,theObject.birthType))

    get_birth_type(mammal1)
    get_birth_type(reptile1)

main()