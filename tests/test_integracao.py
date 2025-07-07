import unittest
from app.clima_api import ClimaAPI

class TestObterClimaIntegracao(unittest.TestCase):

    def test_obter_clima_api_real(self):
        api_key = "d548cc1e53515004d6b4f2b22e0b338c"
        url = "https://api.openweathermap.org/data/2.5/weather"
        cidade = "São Paulo"

        clima_api = ClimaAPI(api_key=api_key, url=url)
        resultado = clima_api.obter_clima(cidade)

        # Verifica se os principais dados existem no retorno
        self.assertEqual(resultado["cidade"], cidade)
        self.assertIsInstance(resultado["actual_temp"], (int, float))
        self.assertIn("description", resultado)
        self.assertIn("lat", resultado)
        self.assertIn("lon", resultado)

if __name__ == "__main__":
    unittest.main()