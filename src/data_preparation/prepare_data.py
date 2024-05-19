import pandas as pd
from datetime import datetime
import chardet

def detect_encoding(file_path):
    """Detecta a codificação do arquivo."""
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

def load_data(file_path):
    """Carrega dados brutos do arquivo CSV com a codificação detectada."""
    encoding = detect_encoding(file_path)
    print(f"Detected encoding: {encoding}")
    return pd.read_csv(file_path, encoding=encoding)

def clean_data(df):
    """Limpa e pré-processa os dados."""
    # Convertendo tipos de dados
    df['Data_Contratacao'] = pd.to_datetime(df['Data_Contratacao'], errors='coerce')
    df['Data_Desligamento'] = pd.to_datetime(df['Data_Desligamento'], errors='coerce')
    
    # Tratar valores nulos na Data_Desligamento
    df['Data_Desligamento'] = df['Data_Desligamento'].fillna(pd.Timestamp(datetime.now()))
    
    # Calculando tempo de permanência em dias
    df['Tempo_Permanencia'] = (df['Data_Desligamento'] - df['Data_Contratacao']).dt.days
    
    # Ajustar a coluna Desligamento para funcionários ainda ativos
    df['Desligamento'] = df['Desligamento'].fillna(0).astype(int)
    
    return df

def save_data(df, file_path):
    """Salva os dados limpos em um arquivo CSV."""
    df.to_csv(file_path, index=False, encoding='utf-8')  # Salve com UTF-8

if __name__ == "__main__":
    raw_data_path = 'data/raw/dados_brutos.csv'
    processed_data_path = 'data/processed/dados_processados.csv'
    
    df = load_data(raw_data_path)
    df_cleaned = clean_data(df)
    save_data(df_cleaned, processed_data_path)
