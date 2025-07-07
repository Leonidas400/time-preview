from app.clima_api import ClimaAPI
from app.app import app

if __name__ == "__main__":
    """
    clima = ClimaAPI(api_key="d548cc1e53515004d6b4f2b22e0b338c", url = 'https://api.openweathermap.org/data/2.5/weather')
    resposta = clima.obter_clima("Goiânia")
    for key, value in resposta.items():
        print(f"{key} : {value}")"""
    app.run(host="0.0.0.0", port=5000, debug=True)
