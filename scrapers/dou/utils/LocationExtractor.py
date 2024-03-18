from data.location.Location import Location


def extractLocationsList(rawLocationStr: str) -> list[str]:
    locationStrList = rawLocationStr.split(', ')
    locations: list[Location] = []
    for locationStr in locationStrList:
        splitLocationStr = locationStr.split(' (')
        if len(splitLocationStr) == 1:
            locations.append(Location(locationStr, 'Ukraine'))
            continue

        city = splitLocationStr[0]
        country = splitLocationStr[1].split(')')[0]
        locations.append(Location(city, country))
    return locations
