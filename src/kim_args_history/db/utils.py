import pandas as pd
#from tabulate import tabulate

def read_data(path='~/data/parquet'):
    df = pd.read_parquet(path)
    return df

def top(cnt=5, dt='2024-07-12'):
    df = read_data()
    fdf = df[df['dt'] == dt]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(cnt)
    
    sdf = sdf.drop(columns=['ymd'])
    ddf = sdf.drop(columns=['dt']).head(cnt)

    r = ddf.to_string(index=False)
    return r

def count(query):
    df = read_data()
    fdf = df[df['cmd'].str.contains(query)]
    cnt = fdf['cnt'].sum()
    return cnt
