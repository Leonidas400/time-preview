# Previsão do Tempo - Projeto Flask

Este é um projeto de aplicação web que mostra a previsão do tempo de uma cidade inserida pelo usuário. Foi desenvolvido em **Python** com o framework **Flask**, e utiliza a **API da OpenWeatherMap** para consultar dados climáticos em tempo real. A aplicação conta com um design responsivo e é facilmente executável via **Docker**.

---

## Tecnologias e Dependências

Este projeto depende das seguintes bibliotecas e ferramentas:

- Python 3.12
- Flask
- Requests
- pytest 
- pip

Instale as dependências com o seguinte comando:

```bash
pip install flask requests pytest


## Docker

para rodar a aplicação com Docker você deve mapear as portas do container com as portas da sua máquina como no exemplo abaixo:

docker container run -p 8080:5000 time-preview