import pandas as pd

def col_list(df):
    return [i for i in df.columns]

def col_total(df):
    return [df[i].sum() for i in df.columns]

def col_count(df):
    return [(df[i] != 0).sum() for i in df.columns]

def col_max(df):
    return [df[i].max() for i in df.columns]



def col_summary(df):
    df.drop(df.columns[0], axis=1, inplace = True)
    return pd.DataFrame({
        "Columns": col_list(df),
        "Total": col_total(df),
        "Count": col_count(df),
        "Max": col_max(df)
        })
