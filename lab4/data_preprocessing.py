"""Contains extraction and transformation logic."""
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

DISTANCE_DS_PATH = 'data/distance.csv'
ORDER_DS_PATH = 'data/order_small.csv'


def read_df(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


truck_df = pd.DataFrame.from_dict({
    "Truck Length": [16.5, 12.5, 9.6],
    "Inner Size (m^2)": [40.25, 30.25, 20.93],
    "Weight Capacity (kg)": [10000, 5000, 2000],
    "Cost Per KM": [3, 2, 1],
    "Speed (km/h)": [40, 35, 30]
})
distances_df = read_df(DISTANCE_DS_PATH)


def get_orders_df() -> pd.DataFrame:
    raw_df = read_df(ORDER_DS_PATH)
    raw_df.loc[:, ['Area', 'Weight']] = raw_df.loc[:, ['Area', 'Weight']] / 10_000

    raw_df['Available_Time'] = pd.to_datetime(raw_df['Available_Time'], format=r'%Y-%m-%d %H:%M:%S').apply(pd.Timestamp.timestamp)
    raw_df['Deadline'] = pd.to_datetime(raw_df['Deadline'], format=r'%Y-%m-%d %H:%M:%S').apply(pd.Timestamp.timestamp)
    
    return raw_df


def get_combined_df() -> pd.DataFrame:
    orders_df = get_orders_df()
    return orders_df.merge(distances_df, how='inner', on=['Source', 'Destination'])


if __name__ == '__main__':
    print(truck_df)
    print(get_combined_df())
    print(distances_df)

