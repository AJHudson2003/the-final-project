# AJ Hudson
# 3.7.19
'this is a queations game that i am using for this '

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
print(average)

print('question three lets have some more fun.')

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

print('questions three')
print('')

