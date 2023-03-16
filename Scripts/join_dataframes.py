import pandas as pd

def join_dataframes(first_dataframe, second_dataframe):
    df_first = pd.read_csv(first_dataframe, decimal=".", )
    df_second =  pd.read_csv(second_dataframe)
    
    return df_first.join(df_second)

data = join_dataframes(r"CSV\populations.csv",r"CSV\ubications.csv",)

data.to_csv(r"CSV\populations_with_ubications.csv", sep=",", index=False,)