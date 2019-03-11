# AJ Hudson
# 3.7.19

welcome = input('Welcome to the Questions game!')
def welcome():
    print("")

print('question number one')
print('')
name = input("What is your name: ")
def greeting():
    print(" hi there " + name + "!")
    print("nice to meet you")
greeting()

print('')
print('questions two!')
print('')
total = 0
how_many_tests = int(input("How many test would you like to average today:  "))
print("")
for i in range(how_many_tests):
    score = float(input("enter score for tests: "))
    total = total + score
average = total / how_many_tests
print("")
print("average: " + str(round(average, 2)))
print(type(average)