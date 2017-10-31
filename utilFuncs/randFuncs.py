def listToLongString(symbList):
    longStr = ""

    for listStr in symbList:
        longStr = longStr + " " + listStr
    return longStr

def lngStringToList(lngString):
    symbList = lngString.split(" ")

    return symbList