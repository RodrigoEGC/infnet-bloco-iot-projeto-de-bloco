# Carta do projeto

## Histórico de Negócios

* O cliente Fernando Ferreira se encontra no ramo de meteorologia.

* Nosso cliente solicita atualizaçoes sobre a predição do clima e recebe alertas quando houver previsão de eventos climaticos relevantes, como tempestades.

## Ecopo
*  Descrever os conceito de big data, análise de dados e machine learning
* Analisar aplicações de análise de dados
* Especificar um sistema de predição baseado em dados
* Implementar um sistema de predição baseado em dados obtidos a partir de sensores IoT

* Trataremos os dados do dataset, para então realizar a simulação rodando na aws,treinando um modelo de aprendizado de máquina de previsão que irá detectar e acionar uma alerta.


## Pessoas
* Envolvidos no projeto:
	* Desenvolvedores:
		* Cristina Andrade
		* Rafael Reis
		* Rodrigo Araujo
	* Cliente:
		* Fernando Ferreira

	
## Metricas
* Sistema de predição do clima, onde os dados são lidos e processados na AWS para então serem teinados para exibir um alerta quando houver possibilidade de tempestades.


## Plano
* A partir do dataset, escolhemos um determinado estado para análise.
* Realizamos a limpeza destes dados eliminando valores nulos
* convertemos os valores de farenheit para celsius.
* Criamos scripts para enviar este novo dataset a AWS.
* Criamos modelos baseados em ARIMA e Facebook Prophet
* Criamos atuadores na AWS, para criamos o Device Shadow e gerar o alerta.
* Geramos o diagrama de fluxo de dados e obtenção de dados.



## Arquitetura

  * Utilizaremos dados do CSV  (https://www.kaggle.com/sudalairajkumar/daily-temperature-of-major-cities)
* Criamos scripts para envio de dados a AWS
	* Utilizaremos python para construção e amostragem
	* Utilização de serviços AWS
	* O medelo utilizado foi Prophet e ARIMA
	


## Comunicação
* As reuniões são realizadas semanalmente, e havendo necessidade nos reunimos mais de uma vez na semana.

* Todos os participantes mantêm contato diretamente com o cliente Fernando, em reuniões realizadas às segundas-feiras e também durante a semana conforme necessidades.

