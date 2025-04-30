class Friend:
    def __init__(self, name, friend):
        self.name = name
        self.__friend = friend #friend is private variable

    def __printFriend(self): #friend is private method
        print(f"{self.__friend} is friend of {self.name}")

    def display(self):
        self.__printFriend()