"""

"""
from clima_api import ClimaAPI
import unittest
from unittest import patch, Mock

class TestObterClima(unittest.TestCase):

    @patch("requests.get")
    def test_get_obter_clima(self, mock_get):
        """
        Nossa requisicao de API vai ter esse dicionario como resposta 'fake'

        O que esta sendo testado e se a funcao obter_clima sabe lidar corretamente com uma resposta no formato esperado da API
        """
        resposta_mock = Mock()
        resposta_mock.status_code = 200

        resposta_mock.json.return_value = {

            "coord":{
                "lon":-46.6361,
                "lat":-23.5475
            },
            "weather":[
                {
                    "id":800,
                    "main":"Clear",
                    "description":"céu limpo",
                    "icon":"01n"
                }
            ],
            "base":"stations",
            "main":{
                "temp":17.2,
                "feels_like":16.86,
                "temp_min":15.61,
                "temp_max":20.25,
                "pressure":1023,
                "humidity":72,
                "sea_level":1023,
                "grnd_level":932
                },
            "visibility":10000,
            "wind":{
                "speed":2.06,
                "deg":30
            },
            "clouds":{
                "all":0
            },
            "dt":1750295719,
            "sys":{
                "type":2,
                "id":2082654,
                "country":"BR",
                "sunrise":1750240033,
                "sunset":1750278494
            },
            "timezone":-10800,
            "id":3448439,
            "name":"São Paulo",
            "cod":200
        }
        
        api = ClimaAPI(api_key="fake_key", url="https://api.openweathermap.org/data/2.5/weather")
        resultado = api.obter_clima("São Paulo")
        
        self.assertEqual(resultado["cidade"], "São Paulo")
        self.assertIn("actual_temp", resultado)
        self.assertIn("description", resultado)
        self.assertIn("lat", resultado)
        self.assertIn("lon", resultado)