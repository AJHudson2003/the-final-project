'''
 AJ Hudson
 3.7.19
 This is a questions game that i am using for this fun questions game. this will ask five random questions for you to answer.
This will be a few questions that will have a few different questions for you to answer.
I hope that you will have

'''
welcome = input('Welcome to the Questions game!')
def welcome():
    print("")
# this will ask your name so they components will be able to identify the person taking the servey.

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
# This will ask the user to enter a few numbers for their test to answer and then it will round it for them.
total = 0
how_many_tests = int(input("How many test would you like to average today:  "))
print("")
for i in range(how_many_tests):
    score = float(input("enter score for tests: "))
    total = total + score
average = total / how_many_tests
print("")
print("average: " + str(round(average, 2)))
print(average)
print('question three lets have some more fun.')
print('')
# This will ask the user that they will have to enter a quad size that they will need to be able to ride.
# This will ask about your quad size for you to ride.
while True:
    quad_size_frame=int(input("enter a size of quad frame you need."))
    if quad_size_frame <= 30:
        print('that size is to small')
    elif quad_size_frame >= 145:
        print('that quad size is way still to big')
    elif quad_size_frame >= 95:
        print('that quad size is to big.')
    else:
        quad_size_frame >= 60
        print('that quad size is the right size!')
        break

print('questions four')
print('')
# this will ask for some numbers that they put in and add them together for them so they don't have to.

sum = 0
for i in range(10):
    enter_a_number=int(input('enter a few numbers: '))
    sum = sum + enter_a_number
print('')
print('the sum of all your numbers is ' + str(sum))

print('question five')
print('')
print("we are going to print a set of two numbers")
# this will have the user input to print out the numbers that they put in.
def two_numbers(a, c = 20):
    print('first number: ', a)
    print('second number: ', c)
two_numbers(3, 79)

two_numbers(30)
print('')

print('thanks for playing my game')
print('i am glad you played my game it means a lot to me!')