# AJ Hudson
# 3.7.19
'this is a queations game that i am using for this '

welcome = input('Welcome to the Questions game!')
def welcome():
    print("")
# this will ask your name.

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

# this will ask about your test sores.
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
# this will ask about your quad size for you to ride.

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
# this will ask for some numbers.

sum = 0
for i in range(10):
    enter_a_number=int(input('enter a few numbers: '))
    sum = sum + enter_a_number
print('')
print('the sum of all your numbers is ' + str(sum))

print('question five')
print('')
print("we are going to print a set of two numbers")
def two_numbers(a, c = 20):
    print('first number: ', a)
    print('second number: ', c)
two_numbers(3, 79)

two_numbers(30)