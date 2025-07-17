import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(animals)
    heavy_df= df[(df['weight']>100)]
    return heavy_df.sort_values(by='weight',ascending=False)[['name']]

    