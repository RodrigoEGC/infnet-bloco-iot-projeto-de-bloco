[![Build Status](https://aws.amazon.com/pt/console/_apis/build/status/data-science-template?branchName=master)](https://aws.amazon.com/pt/console/_build/latest?definitionId=15&branchName=master)

### [Projeto de Bloco - IOT]()

**_ “Implementar um sistema de predição baseado em dados obtidos a partir de sensores de dispositivos IoT
conectados à nuvem, documentando a solução e explicando a modelagem utilizada.” _**


Esta é uma estrutura de diretório de projeto geral para o Team Data Science Process desenvolvida pela Microsoft. Ele também contém modelos para vários documentos que são recomendados como parte da execução de um projeto de ciência de dados ao usar o TDSP.

O Team Data Science Process (TDSP) é uma metodologia ágil e iterativa de ciência de dados para melhorar a colaboração e o aprendizado da equipe. É suportado por meio de uma definição de ciclo de vida, estrutura de projeto padrão, modelos de artefatos e ferramentas para ciência de dados produtiva.

**_NOTA: Nesta estrutura de diretório, a pasta Data NÃO deve conter GRANDES dados brutos ou processados. Ele deve conter apenas conjuntos de dados pequenos e de amostra, que podem ser usados ​​para testar o código_**


* Os dois documentos em Docs/Project ajudam a definir o projeto no início de um contrato e fornecem um relatório final ao cliente ou cliente.

## Conteúdo Gerado do Projeto

```
├── .gitignore           <- Arquivos que devem ser ignorados pelo git.
│                             
│
├── Data
│   ├── Processed            <- Os conjuntos de dados canônicos finais para modelagem.
│   ├── Raw                  <- O despejo de dados original e imutável.
│   ├── Modeling             <- Modelo.
│
├── Docs                 <- Documentação
│   ├── documentation.md     <- Modelo padrão para documentar processos e decisões.
│   ├── Project              <- Projeto.
│   |  └── Charter           <- Descreve o projeto e o objetivo.
│   |  └── FinalReport       <- Final reporte.
│   ├── DataReport           <- Data reporte.
│   |   └── DataDictionary   <- Descrever os dados escolhidos.
│   |   └── Model Reports    <- Reporte.
│   ├── Model                <- Notebooks for modelling
│      └── Model Reports     <- Start page.
│
├── Code                <- Códigos para análise e teste.
│   ├── DataPrep             <- Notebooks para EDA
│   ├── Model                <- Notebooks para Modelo
│   │   └── example1.ipynb   <- Example python notebook
|   |   └── example2.ipynb   <- Example python notebook
|   |   └── example3.ipynb   <- Example python notebook
│   ├── Operationalization   <- Scripts para conexão com a aws
│

```


### Ambiente de desenvolvimento
Configurar um ambiente virtual

#### Setup
```
cd infnet-bloco-iot-projeto-de-bloco
$ docker build . -t sensor_aws

$docker run -it sensor_aws /bin/bash

```

#### Script envio de dados

```
python Code/Operationalization/read_entries_data_set.py
```
#### Script device shadow

```
python Code/Operationalization/shadow_connection.py
```
