from sys import argv

script, user_name, age = argv
prompt = '# '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")

print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}")
lives = input(prompt)

print(f"How old are you? {age}")
years_old = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f'''  Alright, so you said {likes} about liking me.
            you are {years_old} years old... and
            you live in {lives}. Not sure where that is.
            and you have a {computer} computer. Nice!
''')
