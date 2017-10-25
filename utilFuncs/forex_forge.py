from assets import api_key
# urllib.request is for opening and reading URLS
import urllib.request, json

API_KEY = api_key.key

def loadReadUrl(partialUrl):
    with urllib.request.urlopen(partialUrl + API_KEY) as url:
        data = json.loads(url.read().decode())
        return data

def getSymbols():
    urlSym = "https://forex.1forge.com/1.0.2/symbols?api_key="
    return loadReadUrl(urlSym)

def getFxPairs(fxPairs):
    urlFxPairs = "https://forex.1forge.com/1.0.2/quotes?pairs="+ fxPairs +"&api_key="
    return loadReadUrl(urlFxPairs)

def marketStatus():
    urlMktStatus = "https://forex.1forge.com/1.0.2/market_status?api_key="
    return loadReadUrl(urlMktStatus)

def getForgeQuota():
    urlQuota = "https://forex.1forge.com/1.0.2/quota?api_key="
    return loadReadUrl(urlQuota)
