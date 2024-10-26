import os
from google.cloud import bigquery
import streamlit as st

# Introdução
st.title("Tech Challenge Phase 4")
st.header("Introdução")
st.write("""
Bem-vindo a este projeto. Neste projeto, exploraremos os dados, descobriremos insights e tiraremos conclusões.
""")

# Organização dos dados
st.header("Organização do Banco de Dados")
st.write("""
Estrutura dos dados no Big Query
""")

# Debug statement to check if the code reaches this point
st.write("Initializing BigQuery client...")

try:
    # Importação dos dados
    project_id = 'neural-journey-377617'
    client = bigquery.Client(project=project_id)

    query = """
    SELECT * FROM `neural-journey-377617.cars.cars_table` LIMIT 1000
    """
    ipea_df = client.query(query).to_dataframe()

    # Debug statement to check if the query was successful
    st.write("Query executed successfully. Displaying data...")

    # Dados de Exemplo
    st.header("Demonstração dos Dados (tabelas)")
    st.write(ipea_df.head())

    # Exploração de Dados
    st.header("Análise Exploratória de Dados")
except Exception as e:
    st.error(f"An error occurred: {e}")
