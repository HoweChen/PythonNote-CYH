from die import Die

die = Die()

result = []

for roll_num in range(100):
    result = die.roll()
    result.append(result)

print result
