alien_0 = {'color':'green', 'points':5 }
alien_1 = {'color' : 'red', 'points': 6}
alien_3 = {'color': 'yellow', 'points': 15}

aliens = [alien_0,alien_1,alien_3]
print(aliens)

aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5 , 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print('total number of aliens: '+ str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:5]:
    print(alien)

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms','extra cheese'],
}

print('you ordered a' + pizza['crust']+'-crust pizza' + 'with the following toppings: ')

for topping in pizza['toppings']:
    print(topping)


users = {
    'aeinstein':{
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton' ,
    },

    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
    }
}
for username,user_infor in users.items():
    print("username:"+username)
    full_name = user_infor['first']+'  '+user_infor['last']
    location = user_infor['location']
    print("Full_name:"+full_name.title())
    print('location:'+location.title())