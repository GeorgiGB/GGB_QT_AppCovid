import urllib.request
import json

url='https://dadesobertes.gva.es/va/api/3/action/datastore_search?resource_id=14c5eb17-30cf-46e8-9564-7051a841c549&limit=542'

jsonData = None

with urllib.request.urlopen(url) as response:
    jsonCovid = response.read()
    jsonData = json.loads(jsonCovid.decode("utf-8"))
    print(jsonData)
    print("###################################################")
    for x in range(0,542):
        municipios = jsonData['result']['records'][x]['Municipi']
        casos = jsonData['result']['records'][x]['Casos PCR+ 14 dies']
        
        print("Municipio: ", municipios, "|| Infectados: ", casos)
        