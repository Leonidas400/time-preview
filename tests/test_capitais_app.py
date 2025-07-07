from app.clima_api import ClimaAPI
from app.capitais_app import obter_info_capitais  

api = ClimaAPI(
    api_key="d548cc1e53515004d6b4f2b22e0b338c",  
    url="https://api.openweathermap.org/data/2.5/weather"
)

dados = obter_info_capitais(api)

for item in dados:
    print(f"{item['cidade']}: {item['temperatura']}°C")