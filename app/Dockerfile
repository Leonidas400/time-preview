FROM python:3.12.1
#puxando a imagem do python na versão 3.12.1

WORKDIR /app
#definindo o diretório de trabalho para o dockerfile

COPY . .
#copiando todo o conteúdo da pasta app

RUN pip install --no-cache-dir -r requirements.txt
#comandos para instalar as dependencias necessárias

RUN pytest -v --maxfail=1 --disable-warnings
#roda o pytest durante o build da imagem, enquanto a imagem é contruida ela executa e mostra o status do test e se tiver um erro a construção falha

EXPOSE 5000
#expondo a porta 5000 do container para mapeamento e definição de uma porta definida

CMD ["python3", "main.py"]
#comandos que serão executados no terminal
