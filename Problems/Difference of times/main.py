# put your python code here
first_hour = int(input())
first_minutes = int(input())
first_seconds = int(input())
second_hour = int(input())
second_minutes = int(input())
second_seconds = int(input())

first = (first_hour * 60 * 60)
first += first_minutes * 60
first += first_seconds

second = (second_hour * 60 * 60)
second += second_minutes * 60
second += second_seconds
print(second - first)
