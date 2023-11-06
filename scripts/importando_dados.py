import sqlite3
import pandas as pd

connection = sqlite3.connect('mydata.db')  # Replace with the path to your SQLite database file

dict_caminho_nome = {
    'maio_2020': 'dados_projeto/PNAD_COVID_052020/PNAD_COVID_052020.csv',
    'junho_2020': 'dados_projeto/PNAD_COVID_062020/PNAD_COVID_062020.csv',
    'julho_2020': 'dados_projeto/PNAD_COVID_072020/PNAD_COVID_072020.csv',
    'agosto_2020': 'dados_projeto/PNAD_COVID_082020/PNAD_COVID_082020.csv',
    'setembro_2020': 'dados_projeto/PNAD_COVID_092020/PNAD_COVID_092020.csv',
    'outubro_2020': 'dados_projeto/PNAD_COVID_102020/PNAD_COVID_102020.csv',
    'novembro_2020': 'dados_projeto/PNAD_COVID_112020/PNAD_COVID_112020.csv',
}

for nome, caminho in dict_caminho_nome.items():
    df = pd.read_csv(caminho)  # Read the CSV file into a Pandas DataFrame
    df.to_sql(nome, connection, if_exists='replace', index=False)  # Write the DataFrame to the SQLite database

connection.close()
