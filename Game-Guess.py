
# coding: utf-8

# In[2]:


__author__ = 'Sahar'

from random import randint
random_number = randint(1, 8)
print(random_number)
guesses_left = 3
while guesses_left >= 0:
  guess=int(input("gues a number: ")) 
  if guess==random_number:
    print("you win!")
    break
  guesses_left = guesses_left -1
else:
    print ("you lose!")

