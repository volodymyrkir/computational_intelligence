"""Contains extraction and transformation logic."""
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

DISTANCE_DS_PATH = 'data/distance.csv'
ORDER_DS_PATH = 'data/order_large.csv'


def read_df(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


truck_df = pd.DataFrame.from_dict({
    "Truck Type (length in m)": [16.5, 12.5, 9.6],
    "Inner Size (m^2)": ["16.1x2.5", "12.1x2.5", "9.1x2.3"],
    "Weight Capacity (kg)": [10000, 5000, 2000],
    "Cost Per KM": [3, 2, 1],
    "Speed (km/h)": [40, 35, 30]
})
distances_df = read_df(DISTANCE_DS_PATH)


def get_orders_df() -> pd.DataFrame:
    raw_df = read_df(ORDER_DS_PATH)
    raw_df.loc[:, ['Area', 'Weight']] = raw_df.loc[:, ['Area', 'Weight']] / 10_000
    return raw_df


def get_combined_df() -> pd.DataFrame:
    orders_df = get_orders_df()
    return orders_df.merge(distances_df, how='inner', on=['Source', 'Destination'])


if __name__ == '__main__':
    print(truck_df)
    print(get_combined_df())
    print(distances_df)

