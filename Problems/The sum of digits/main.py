# put your python code here
digits = int(input())
first_digit = digits // 100
rest = digits % 100
second = rest // 10
third = rest % 10
print(first_digit + second + third)
