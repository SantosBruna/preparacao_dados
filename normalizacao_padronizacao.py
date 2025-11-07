import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler


pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

df = df[['idade', 'salario']]

# Normalização - MinMaxScaler
scaler = MinMaxScaler() # criando o modulo do scaler - aqui ele normaliza no padrão 0 e 1. Aqui é normalizado os dadsos.
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1)) # aqui com o feature_range pode ser definido o valor minimo e o valor maximo
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform((df[['salario']]))

# Padronização - StandardScaler utiliza a média zero e desvio padrão
scaler = StandardScaler() # Aqui é feita uma padronização dos dados
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

# Padronização - RobustScaler aqui utiliza a mediana e o qr
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRObustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))
























