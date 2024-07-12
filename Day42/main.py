# import random

# def get_choices():
#     choice = ["rock","paper","scissors"]
#     choice = [x.upper() for x in choice]
#     player_choice = input("Enter a choice (rock,paper,scissors): ").upper()
#     computer_choice = random.choice(choice)
#     choice = {
#         "player_choice":player_choice,
#         "computer_choice":computer_choice
#     }
#     return choice


# def check_win(player, computer):
#     print(f"You choose {player} and computer choose {computer}")
#     if player == computer:
#         print("It's a tie !")
#     elif player == "ROCK" and computer == "PAPER":
#         print("Paper covers rock you lost the game.")
#     elif player == "ROCK" and computer == "SCISSORS":
#         print("Rock breaks scissors. You won the game!")
#     elif player == "PAPER" and computer == "ROCK":
#         print("Paper covers rocks you won")
#     elif player == "PAPER" and computer == "SCISSORS":
#         print("Scissors cuts paper you lost the game")
#     elif player == "SCISSORS"  and computer == "ROCK":
#         print("Rock breaks scissors. You lost the game")
#     elif player == "SCISSORS" and computer == "PAPER":
#         print("Scissors cuts paper. You won")
#     else:
#         print("Not handled")

# choice = get_choices()
# player = choice.get("player_choice")
# computer = choice.get("computer_choice")
# check_win(player,computer)
# choice = get_choices()
# print(choice)

# food = ["pizza","carrots","eggs"]
# print(random.choice(food))

# choice = get_choices()
# print(choice)

# name = "Beautiful"
# phrase = "Beau" + " is my name"
# print(phrase)

# name = "Keshab"
# print("b" in name)
# print(len(name))

# name = "Bea\""
# print(name)

# name = "Beau is cool"
# print(name[1:7])

# if -5:
#     print("yes")

# book = all([0,""])
# print(book)

# num1 = 2+3j
# num2 = complex(2,3)

# print(num1,num2)

# print(abs(num1))

# from enum import Enum

# class State(Enum):
#     INACTIVE = 0
#     ACTIVE = 1

# print(list(State) )

# dogs = ["dog1","dog2","dog3"]
# cats = ["cat1","cat2","cat3"]
#
# print(dogs)
# dogs[2] = "Bruno"
# print(dogs)
# print(len(dogs))
# dogs.append("kale")
# print(dogs)
# print(dogs)


# dogs.extend(cats)
# print(dogs)

# print(names[0])
# print(names.index("Roger"))


# names = ("apple","syd","roger")
# names2 =["apple","syd","roger"]

# print(sorted(names2))

# set1 = {"Roger","Syd"}
# set2 = {"Roger","Syd"}

# print(set1.issubset(set2))

# def count():
#     count = 0

#     def increment():
#         count = count + 1
#         print(count)

#     increment()

# count()

# def counter():
#     count = 0

#     def increment():
#         nonlocal count
#         count = count + 1
#         return  count





#     return increment

# increment = counter()

# print(increment())
# print(increment())
# print(increment())

# age = 34
# print(id(age)

# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def give_intro(self):
#         print(f"Hello my name is {self.name} and I am {self.age} years old")
        

# kale = Dog("Kale",25)
# kale.give_intro()

# import lib.dog as dog
# dog.bark()

# import math

# print(int(math.sqrt(4)))

# keshab = lambda num: num*2

# print(keshab(2))

# map,filter and reduce

# numbers = [1,2,3]
# def double(a):
#     return 2*a

# result = map(double,numbers)
# # print(result)
# for x in result:
#     print(x)

# Using map to square numbers
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# numbers = (x for x in range(10))

# even_numbers = [x for x in numbers if x%2==0]
# print(even_numbers)

# even_numbers = list(filter(lambda x:x%2==0,numbers))
# print(even_numbers)
