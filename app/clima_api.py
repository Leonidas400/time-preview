import requests

class ClimaAPI:
    def __init__(self, api_key, url):
        self.api_key = api_key
        self.url = url
    
    def obter_clima(self, cidade):
        """
        Consulta o clima atual de uma cidade usando a API OpenWeather.
        Params:
            cidade (str): Nome da cidade.
        Returns:
            dict: Dicionario com temperatura, sensacao termica, umidade, vento, descricao e min/max.
        """

        # Resposta da API
        params = {
        'q': cidade,
        'appid': self.api_key,
        'units': 'metric',
        'lang': 'pt_br'
        }
        response = requests.get(self.url, params=params)

        # Tratando a resposta da API
        if response.status_code != 200:
            print(f"Erro na requisicao: {response.status_code}")
        else:
            data = response.json()
            return {
                "cidade": cidade.title(),
                "actual_temp": data['main']['temp'],
                "feels_like": data['main']['feels_like'],
                "humidity": data['main']['humidity'],
                "wind_speed": data['wind']['speed'],
                "description": data['weather'][0]['description'],
                "temp_min": data['main']['temp_min'],
                "temp_max": data['main']['temp_max'],
                "lat": data['coord']['lat'],
                "lon": data['coord']['lon']
            }