class ClubMembers:
    def __init__(self, name, age, food, goal):
        self.name = name
        self.age = age
        self.food = food
        self.goal = goal

    def displayInfo(self):
        print(self.name)
        print(self.age)
        print(self.food)
        print(self.goal)

class ClubOfficers(ClubMembers):
    def __init__(self, name, age, food, goal, position):
        self.name = name
        self.age = age
        self.food = food
        self.goal = goal
        self.position = position

    def portrayInfo(self):
        print(self.name)
        print(self.age)
        print(self.food)
        print(self.goal)
        print(self.position)

member1 = ClubMembers('Tom', 14, 'Ice Cream', 'To be Happy')
member2 = ClubOfficers('Vera', 16, 'Beemf', 'Chef', 'Treasurer')
print(member1.name)
print(member1.age)
print(member1.food)
print(member1.goal)
print('-----------')
print(member2.name)
print(member2.age)
print(member2.food)
print(member2.goal)
print(member2.position)