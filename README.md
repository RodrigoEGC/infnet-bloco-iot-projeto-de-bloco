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
│   ├── DataPrep             <- Notebooks for generating and analysing features (1 per feature)
│   ├── Model                <- Notebooks for EDA
│   │   └── example1.ipynb   <- Example python notebook
|   |   └── example2.ipynb   <- Example python notebook
|   |   └── example3.ipynb   <- Example python notebook
│   ├── Operationalization   <- Notebooks for modelling
│
├── scripts             <- Scripts
│   ├── deploy               <- Scripts MLOps para implantação (WIP)
│   │   └── score.py         <- Script de pontuação
│   ├── train                <- Scripts MLOps para treinamento
│   │   ├── submit-train.py  <- Script para enviar uma execução de treinamento ao Serviço da AWS.
│   │   ├── submit-train-local.py <- Script para treinamento local usando o AWS ML
│
└── tests                    <- Casos de teste (nomeados após o módulo)
    ├── test_notebook.py     <- Exemplo de teste que os notebooks Jupyter executam sem erros
    ├── examplepackage       <- testes de pacote de exemplo
        ├── examplemodule    <- testes de módulo de exemplo (1 arquivo por método testado)
        ├── features         <- testes de recursos
        ├── io               <- teste de io
        └── pipeline         <- teste de pipeline
```


### Ambiente de desenvolvimento
Configurar um ambiente virtual

#### Setup
```
cd infnet-bloco-iot-projeto-de-bloco
python -m venv dst-env
```

#### Activate environment
Max / Linux
```
source dst-env/bin/activate
```

Windows
```
dst-env\Scripts\activate
```

