# put your python code here
duration_days = int(input())
food_cost_day = int(input())
flight_cost = int(input())
one_night_hotel = int(input())

sum_cost = ((duration_days * food_cost_day)
            + (flight_cost * 2)
            + (one_night_hotel * (duration_days - 1)))

print(sum_cost)
