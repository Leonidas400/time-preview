FROM python:3.12.1
#puxando a imagem do python na versão 3.12.1

WORKDIR /app
#definindo o diretório de trabalho para o dockerfile

COPY . .
#copiando todo o conteúdo da pasta app

RUN pip install --no-cache-dir requests flask pytest
#comandos para instalar as dependencias necessárias

EXPOSE 5000
#expondo a porta 5000 do container para mapeamento e definição de uma porta definida

CMD ["python3", "main.py"]
#comandos que serão executados no terminal
