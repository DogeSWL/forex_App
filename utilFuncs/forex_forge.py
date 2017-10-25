from assets import api_key
import urllib.request, json

API_KEY = api_key.key

def loadReadUrl(partialUrl):
    with urllib.request.urlopen(partialUrl + API_KEY) as url:
        data = json.loads(url.read().decode())
        return data

def getSymbols():
    return loadReadUrl("https://forex.1forge.com/1.0.2/symbols?api_key=")

def getForgeQuota():
    return loadReadUrl("https://forex.1forge.com/1.0.2/quota?api_key=")
