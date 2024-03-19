#Practical task 2
#code to output the pattern, using if-else statement in combination with a single for loop.

row_count = 5
start = 1
end = (2 * row_count)
for row_number in range(start, end):
       star_count = row_number if row_number <= row_count else end - row_number
       print("*" * star_count)