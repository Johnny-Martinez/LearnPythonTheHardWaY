# Variable for types of people as in 1 and 0.
types_of_people = 10
# Formatted string with a variable inside.
x = f"There are {types_of_people} types of people."

# Variable for string binary
binary = "binary"
# Variable for string don't.
do_not = "don't"
# Variable for formatted string with variables.
y = f"Those who know {binary} and those who {do_not}"

# Print left side of string.
print(x)
# print right side of string.
print(y)
# print formatted string with x variable
print(f"I said: {x}")
# print formatted string with y variable.
print(f"I also said: '{y}' ")

# Boolean Expression
hilarious = False
# Variable for string with boolean expression resulting in false due to empty {}.
joke_evaluation = "Isn't that joke so funny??? {}"

# Print variable joke_evaluation calling on .format() method and passing in variable hilarious.
print(joke_evaluation.format(hilarious))


w = "This is the left side of... "
e = "a string with a right side."

# printing variables w and e together.
print(w + e)
