import pandas as pd
from collections import Counter





def name_columns(item_column, component_names):
    if type(item_column) != str:
        raise TypeError("item column must be a string")
    if type(component_names) != list:
        raise TypeError("component names must be a list of strings")
    
    columns = [item_column]
    for i in component_names:
        columns.append(i)
    return columns

def construct_items_column(data):
    items = []
    for row in data.to_numpy():
        for i in row:
            items.append(i.lower())
    return items

def construct_component_count_rows(df):
    items = df.iloc[:,0]
    for i in items:
            # Extract the components for the current item
            components = [component for component in i]
            # Count the occurrences of each component
            counts = Counter(components)
            
            # Update the corresponding row of the DataFrame with the component counts
            df.loc[df.iloc[:, 0] == i, df.columns[1:]] = [counts.get(comp, 0) for comp in df.columns[1:]]

def build_df(data, item_column, component_names):
    
    columns = name_columns(item_column, component_names)
    words = construct_items_column(data)

    df = pd.DataFrame(columns=columns)
    df[item_column] = words
    construct_component_count_rows(df)
    return df


