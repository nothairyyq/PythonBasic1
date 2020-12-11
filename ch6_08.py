cities = {
    'suzhou' : {
        'country' : 'China',
        'people' : '14billion',
        'fact' : 'suzhou is the beautiful citiy',
    },
    'shanghai' : {
        'country' : 'China',
        'people' : '五百万',
        'fact' : 'shnaghai is the economy city',
    }
}

for city in  cities:
    for city_info in cities[city].values():
        print(city+" information are: "+city_info)