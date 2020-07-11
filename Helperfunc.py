import pandas as pd

def Import_Df(dataset_link):
    df = pd.read_csv(dataset_link)
    df = df.dropna()
    return df

def Display_Op():
    pd.options.display.max_columns = None

x = 2
def addition(number):
    return number + 1