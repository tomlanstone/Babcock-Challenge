def query_df(df,col,val):
    result = []
    for index, row in df.iterrows():
        if row[col] == val:
            result.append(row["Letter"])
    return result

def loop_query_df(df, col):
    out = {}
    for i in range(1,df[col].max()):
        result = query_df(df,col,i)
        for ii in result:
            out[ii] = i
    return out