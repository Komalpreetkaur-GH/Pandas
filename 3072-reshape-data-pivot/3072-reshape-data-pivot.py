import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(weather)
    pivot_table1=pd.pivot_table(df,index='month',columns='city',values='temperature')
    return pivot_table1
    