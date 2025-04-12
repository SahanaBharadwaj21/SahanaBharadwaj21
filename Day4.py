import random
# import my_module
# random_integer = random.randint(1,20)
# print(random_integer)
# print(my_module.my_fav_num)

# random_int = random.randint(0,1)
# if random_int == 0:
#     print("heads")
# else:
#     print("Tails")


rock ='''
    ___________
---'     ______)
        (_______)
        (_______)
        (______)
----. __ (____)

'''

paper= '''
    ________
---'     ___)____
        (________)
        (_________)
        (________)
----. __ (______)


'''

scissors ='''
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.


'''

games = [rock,paper,scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
if user_input >= 0 and user_input <=2 :
    print(games[user_input])


computer_choice = random.randint(0,2)
print("Computer chose: ")
print(games[computer_choice])

if user_input >= 3 or user_input < 0:
    print("invalid")
elif user_input == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_input ==2:
    print("You lose!") 
elif computer_choice > user_input:
    print("You lose!") 
elif user_input > computer_choice:
    print("You win!")
elif computer_choice == user_input:
    print("It's a Draw")

