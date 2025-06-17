rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

list_answer = [rock, paper, scissors]

# My answer

my_answer = int(input('What do you choose? Type 0 for Rock, 1, for Paper or 2 for Scissors.\n'))
my_result = list_answer[my_answer]

# Computer answer

computer_answer = random.randint(0,2)
computer_result = list_answer[computer_answer]

print(f"{my_result}\n Computer choose: {computer_result}")

if my_answer == computer_answer:
    print('Draw')
elif my_answer == 0 and computer_answer == 1:
    print('You lose')
elif my_answer == 1 and computer_answer == 2:
    print('You lose')
elif my_answer == 2 and computer_answer == 0:
    print('You lose')         
else:
    print('You won')