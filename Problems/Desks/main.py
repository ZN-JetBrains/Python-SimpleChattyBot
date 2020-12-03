# put your python code here
class_one = int(input())
class_two = int(input())
class_three = int(input())

if class_one % 2 == 1:
    class_one += 1

if class_two % 2 == 1:
    class_two += 1

if class_three % 2 == 1:
    class_three += 1

desks = (class_one + class_two + class_three) // 2
print(desks)
