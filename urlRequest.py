import urllib.request
import json

url='https://dadesobertes.gva.es/va/api/3/action/datastore_search?resource_id=14c5eb17-30cf-46e8-9564-7051a841c549&limit=542'

jsonData = None


class urlRequest:
    def __init__(self):

        self.arrayVlc = []
        self.arrayCastellon = []
        self.arrayAlicante = []

        with urllib.request.urlopen(url) as response:
            jsonCovid = response.read()
            jsonData = json.loads(jsonCovid.decode("utf-8"))

            # Recorremos el api para coger la informacion y almacenarla por municipios
            for x in range(0, 542):

                if str(jsonData['result']['records'][x]['CodMunicipio']).startswith('46'):
                    self.arrayVlc.append(jsonData['result']['records'][x])

                if str(jsonData['result']['records'][x]['CodMunicipio']).startswith('12'):
                    self.arrayCastellon.append(jsonData['result']['records'][x])

                if str(jsonData['result']['records'][x]['CodMunicipio']).startswith('3'):
                    self.arrayAlicante.append(jsonData['result']['records'][x])
