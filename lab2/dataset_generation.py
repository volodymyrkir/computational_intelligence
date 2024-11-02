"""Contains logic for Self Drive Car dataset generation."""
from random import random

import numpy as np
import pandas as pd

MAX_SPEED, MIN_SPEED = 150, 0
MAX_DISTANCE = 100
ROAD_CONDITIONS = ('dry', 'wet')
FREE_ROAD_PERCENTAGE = 0.6


def create_dataset(
        num_samples: int,
        max_speed: float = MAX_SPEED,
        min_speed: float = MIN_SPEED,
        road_conditions: tuple[str] = ROAD_CONDITIONS,
        free_road_percentage: float = FREE_ROAD_PERCENTAGE,
) -> pd.DataFrame:
    """
    Creates dataset based on parameters of the car, it's environment and amount of samples provided.

    Args:
        num_samples (int): number of samples to generate.
        max_speed (float): maximum possible speed of the car. Defaults to 150.
        min_speed (float): minimum possible speed of the car. Defaults to 0.
        road_conditions (tuple[str]): all possible weather conditions. Defaults to ('dry', 'wet').
        free_road_percentage (float): percentage of the samples without distance to obstacles. Defaults to 0.6.

    Returns:
        pd.DataFrame: Generated dataframe.
    """
    data = {
        'distance_to_obstacle': np.array([
            val if random() > free_road_percentage else None
            for val in np.random.uniform(0, MAX_SPEED, num_samples)
        ]).astype(float),  # Відстань до об'єкта у мертрах

        'vehicle_speed': np.round(
            np.random.uniform(min_speed, max_speed, num_samples),
            decimals=3
        ),  # Швидкість автомобіля в км/год

        'road_condition': np.random.choice(road_conditions, num_samples),  # Стан дороги
    }
    return pd.DataFrame(data)


if __name__ == '__main__':
    df = create_dataset(200)
    print(df)
