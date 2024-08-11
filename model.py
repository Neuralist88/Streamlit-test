import opendatasets as od 
import pandas as pd

# Загружаем датасет из Kaggle

od.download('https://www.kaggle.com/datasets/aaronnorman/2023-global-prosperity-index-w-region-politics/data')

# Сохраняем загруженный датасет в виде датафрейма
def open_data(data_path = '2023-global-prosperity-index-w-region-politics/global_prosperity_regions_politics.csv'):
    df = pd.read_csv(data_path)
    return df



