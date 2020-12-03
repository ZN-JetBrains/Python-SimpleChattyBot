initial_sum = int(input())
number_of_years = 0

while initial_sum < 700_000:
    initial_sum *= 1.071
    number_of_years += 1

print(number_of_years)
