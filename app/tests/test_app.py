from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../html-copy', static_folder='../static')

class MockClimaAPI:
    def obter_clima(self, cidade):
        return {
            "cidade": cidade.title(),
            "actual_temp": "25°C",
            "feels_like": "27°C",
            "humidity": "60",
            "wind_speed": "5",
            "description": "céu limpo",
            "temp_min": "20°C",
            "temp_max": "28°C",
            "lat": -23.55,
            "lon": -46.63
        }


# Instancia da API com sua chave
api = MockClimaAPI()

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
                    "umidade": f"{resposta['humidity']}",
                    "velocidade_vento": f"{resposta['wind_speed']}",
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

                
        
    return render_template("index.html", dados=dados)
    

if __name__ == "__main__":
  app.run(debug=True)
