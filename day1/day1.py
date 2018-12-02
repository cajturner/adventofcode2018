
# Task 1
with open('day1input.txt') as f:
    input = f.readlines()

sanatised_input = [ int(item) for item in input ]
frequency = 0

for item in sanatised_input:
    frequency += item

print (frequency)

# Task 2
frequency = 0
known_frequencies = {frequency}
duplicate_found = False
iterations = 0
while duplicate_found is False:

    for item in sanatised_input:
        frequency += item
        if frequency in known_frequencies:
            print(frequency)
            print(iterations)
            duplicate_found = True
            break
        known_frequencies.add(frequency)
    iterations += 1
