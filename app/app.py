from flask import Flask, render_template, request
from app.clima_api import ClimaAPI
from app.capitais_app import obter_info_capitais

app = Flask(__name__, template_folder='html-copy')

# Instancia da API com sua chave
api = ClimaAPI(
    api_key="d548cc1e53515004d6b4f2b22e0b338c",
    url="https://api.openweathermap.org/data/2.5/weather"
)

@app.route("/", methods=["GET", "POST"])
def home():
    dados = {
        "cidade": "São Paulo",
        "temperatura": "22°C",
        "descricao": "Parcialmente nublado"
    }

    if request.method == "POST":
        cidade = request.form.get("cidade")
        if cidade:
            resposta = api.obter_clima(cidade)
            if resposta:
                dados = {
                    "cidade": resposta["cidade"],
                    "temperatura": f"{resposta['actual_temp']}",
                    "sensacao_termica": f"{resposta['feels_like']}",
                    "descricao": resposta["description"],
                    "umidade": f"{resposta["humidity"]}",
                    "velocidade_vento": f"{resposta["wind_speed"]}",
                    "temp_minima": f"{resposta['temp_min']}",
                    "temp_maxima": f"{resposta['temp_max']}",
                    "lat": resposta["lat"],
                    "lon": resposta["lon"]
                }
            else:
                dados = {
                    "cidade": cidade.title(),
                    "temperatura": "N/A",
                    "descricao": "Cidade não encontrada"
                }
    capitais_info = obter_info_capitais(api)

    return render_template("index.html", dados=dados, capitais=capitais_info)
