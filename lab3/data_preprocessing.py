"""Contains extraction and transformation logic."""
import pandas as pd

DS_PATH = 'dataset.csv'

def read_dataset() -> pd.DataFrame:
    return pd.read_csv(DS_PATH)


def categorical_to_numeric(column: pd.Series) -> pd.Series:
    # The warning is raised because we are replacing from str to int
    unique_values = column.unique().tolist()
    mapping = {value: index for index, value in enumerate(unique_values)}
    print(f'For column - {column.name}, created mapping - {mapping}')
    return column.replace(mapping)


if __name__ == '__main__':
    df = read_dataset()

    print(df)
    new_gender = categorical_to_numeric(df['Gender'])
    print(new_gender.value_counts())