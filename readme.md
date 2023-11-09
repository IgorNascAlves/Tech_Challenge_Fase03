
## Índice

- [O Problema](#o-problema)
- [PNAD-COVID-19 do IBGE](#pnad-covid-19-do-ibge)
- [Solução do projeto](#solução-do-projeto)
    - [Arquitetura do projeto](#arquitetura-do-projeto)
    - [Estrutura de Pastas](#estrutura-de-pastas)
    - [Resultados](#resultados)

# O Problema

Imagine agora que você foi contratado(a) como Expert em Data Analytics por um grande hospital para entender como foi o comportamento da população na época da pandemia da COVID-19 e quais indicadores seriam importantes para o planejamento, caso haja um novo surto da doença.
    
Apesar de ser contratado(a) agora, a sua área observou que a utilização do estudo do PNAD-COVID 19 do IBGE seria uma ótima base para termos boas respostas ao problema proposto, pois são dados confiáveis. Porém, não será necessário utilizar todas as perguntas realizadas na pesquisa para enxergar todas as oportunidades ali postas.

É sempre bom ressaltar que há dados triviais que precisam estar no projeto, pois auxiliam muito na análise dos dados:

* Características clínicas dos sintomas;
* Características da população;
* Características econômicas da sociedade.

# PNAD-COVID-19 do IBGE

O Head de Dados pediu para que você entrasse na base de dados do 
[PNAD-COVID-19 do IBGE](https://covid19.ibge.gov.br/pnad-covid/)
e organizasse esta base para análise, utilizando Banco de Dados em Nuvem e trazendo as seguintes características:

a. Utilização de no máximo 20 questionamentos realizados na pesquisa;

b. Utilizar 3 meses para construção da solução;

c. Caracterização dos sintomas clínicos da população;

d. Comportamento da população na época da COVID-19;

e. Características econômicas da Sociedade;
        

Seu objetivo será trazer uma breve análise dessas informações, como foi a organização do banco, as perguntas selecionadas para a resposta do problema e quais seriam as principais ações que o hospital deverá tomar em caso de um novo surto de COVID-19.
        
# Dica:

- Leiam com atenção a base de dados e toda a documentação que o site o PNAD – Covid19 traz, principalmente os dicionários, que ajudam e muito no entendimento da Base de Dados. 
-  o que já foi ensinado e consolidado nas outras fases para apresentar a resolução do projeto.

# Solução do projeto

## Arquitetura do projeto

![image](https://github.com/IgorNascAlves/Tech_Challenge_Fase03/assets/26041581/001bd63d-e342-4ce6-86c4-bea015563643)

## Estrutura de Pastas

### Análises:
Pasta contendo o arquivo do Power BI onde criamos nossos gráficos e o dashboard.

### Dados do Projeto:
Pasta que armazena os dados utilizados no projeto (não disponibilizados no GitHub devido ao tamanho).

### Dados Tratados:
Dados utilizados no dashboard que passaram por tratamento (não disponibilizados no GitHub devido ao tamanho).

### Notebooks:
O arquivo `explorando_dados.ipynb` foi utilizado para realizar tratamentos e estabelecer conexões com bancos de dados na nuvem e on-premise, gerando os dados tratados.

### Ref:
Imagens de referência utilizadas no relatório.

### Relatórios:
PDFs contendo os relatórios técnico e de negócios.

### Scripts:
Código utilizado para carregar os dados em um banco de dados local.

## Resultados

- [Relatório de Negócios](https://github.com/IgorNascAlves/Tech_Challenge_Fase03/blob/main/Relat%C3%B3rios/Impactos%20COVID-19%20-%20Grupo42.pdf)
- [Relatório Técnico](https://github.com/IgorNascAlves/Tech_Challenge_Fase03/blob/main/Relat%C3%B3rios/Impactos%20COVID-19%20-%20Grupo42.pdf)
- [Dashboard](https://github.com/IgorNascAlves/Tech_Challenge_Fase03/blob/main/Analises/Criando-m%C3%A9tricas.pbix)
- Dados Tratados (selecionando as 23 perguntas) (Indisponível)

    






