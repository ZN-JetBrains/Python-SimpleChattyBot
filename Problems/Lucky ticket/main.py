# Save the input in this variable
ticket = input()

# Add up the digits for each half
counter1 = 0
half1 = 0

while counter1 < len(ticket) / 2:
    half1 += int(ticket[counter1])
    counter1 += 1

counter2 = counter1
half2 = 0
while counter2 < len(ticket):
    half2 += int(ticket[counter2])
    counter2 += 1

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
