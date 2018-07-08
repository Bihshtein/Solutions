
routes = {
	'london':['new york','tel aviv','cairo'],
	'cairo':['harare','addis ababa'],
	'tel aviv':['london', 'bangkok'],
	'monaco':['quatar', 'balli'],

}

def is_route_inner(routes, firstCity, origin, dest):
    if origin not in routes:
        return False
    destCities = routes[origin]    
    if dest in destCities:
        return True
    else:
        for city in destCities:                    
            if (firstCity != city and is_route_inner(routes,firstCity, city, dest)):
                return True
        return False
				
def is_route(routes, origin, dest):
    return is_route_inner(routes, origin, origin, dest)
	
print is_route(routes,'tel aviv', 'monaco')
