car = input('What do you want brown car:')
print('Let me see if I can find you a '+ car)

number = input('How many people are dining: ')

if int(number) >=8:
    print("We don't have a table that can accommdoate "+str(number)+' people.')
else:
    print('we have a table')