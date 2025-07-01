from clima_api import ClimaAPI
import random

CAPITAIS = ["Rio Branco", "Macapá", "Manaus", "Belém", "Porto Velho", "Boa Vista", "Palmas",
        "Salvador", "Fortaleza", "São Luís", "João Pessoa", "Recife", "Teresina", "Natal", "Aracaju", "Maceió",
        "Goiânia", "Cuiabá", "Campo Grande", "Brasília",
        "Vitória", "Belo Horizonte", "Rio de Janeiro", "São Paulo",
        "Curitiba", "Florianópolis", "Porto Alegre"]

random.shuffle(CAPITAIS)

def obter_info_capitais(api: ClimaAPI):
    resultado = []
    for cidade in CAPITAIS[:6]:
        clima = api.obter_clima(cidade)
        if clima:
            resultado.append({
                "cidade": cidade,
                "temperatura": clima["actual_temp"]
            })
    return resultado


