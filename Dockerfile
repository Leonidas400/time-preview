FROM python:3.12.1 AS estagio-de-teste
#falando para o docker usar uma imagem pronta que já vem com o python na versão 3.12.1
#nomeando esse estágio da construção da imagem

WORKDIR /app
#define a pasta principal dentro do container sendo /app e todos os comandos subsequentes   
#vão acontecer nessa pasta

COPY . .
#copia todo o conteúdo na raízdo projeto para a pasta /app 

RUN pip install --no-cache-dir -r requirements.txt
#comando para instalar as dependencias necessárias listadas no arquivo requirements.txt 

RUN pytest -s -v --maxfail=1 --disable-warnings
#roda os testes do pytest durante o build da imagem e mostra os detalhes
#caso tenha algum erro interrompe o build da imagem
#oculta avisos também

FROM python:3.12.1 AS estagio-de-execucao 

WORKDIR /app 

COPY --from=estagio-de-teste /app /app
#copiando tudo o que já foi copiado no estágio anterior 
#tranferindo para a pasta app deste estágio

RUN pip install --no-cache-dir -r requirements.txt
#instalando novamente as dependencias

EXPOSE 5000
#informa que a aplicação usará a porta 5000 do container
#facilita o mapeamento de porta fora do container

CMD ["python3", "main.py"]
#comandos que serão executados no terminal
