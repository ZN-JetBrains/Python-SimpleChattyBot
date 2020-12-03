initial_quantity = int(input())
final_quantity = int(input())

half_life = 12
days = 0

while initial_quantity >= final_quantity:
    initial_quantity //= 2
    days += half_life

print(days)
