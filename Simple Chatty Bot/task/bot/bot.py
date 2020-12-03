print("Hello! My name is Aid.")
print("I was created in 2020.")
print("Please, remind me your name.")
user_name = input()
print("What a great name you have, " + user_name + "!")

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " + str(age) + ": that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
number = int(input())
counter = 0
while counter <= number:
    print(str(counter) + " !")
    counter += 1

print("Let's test your programming knowledge.")


def print_question():
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")


print_question()
is_correct = False

while not is_correct:
    answer = int(input())
    if answer is 2:
        is_correct = True
    else:
        print("Please, try again.")

print("Completed, have a nice day!")
print("Congratulations, have a nice day!")
