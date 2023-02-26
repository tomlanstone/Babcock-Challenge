import pandas as pd

from functions.col_summary import col_summary
from functions.combinations import (count_list_combinations,
                                    find_unused_combos)
from functions.loop_query import loop_query_df
from functions.separate_words import build_df
from functions.generate_random_data import generate_random_data, generate_components

components = list("abcdefghijklmnopqrstuvwxyz")

data = pd.read_csv("data.csv", header=None)
df = build_df(data, "Words", components)

'''
components = generate_components()
data = generate_random_data(100,8)
df = build_df(data,"Items",components)
#'''
## Currently breaks when generating the item column 


all_possible_combinations = count_list_combinations(components)
combinations_in_data = count_list_combinations(df.iloc[:,0])
unused_combinations = find_unused_combos(all_possible_combinations, combinations_in_data)

solution = col_summary(df).rename(columns={"Columns": "Letter"})
solution["Solution"] = solution["Max"]

totals = loop_query_df(solution, "Total")
max = loop_query_df(solution, "Max")

for key in totals:
    if totals[key] <= 5:
        print(key)
