new = '\nTell me something, and I will repeat it back to you: '
new += "\nEnter 'quit ' to end the program. "

active = True
while active:
    message = input(new)

    if message == 'quit':
        active = False
    else:
        print(message)

