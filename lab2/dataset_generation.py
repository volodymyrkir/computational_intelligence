"""Contains logic for Self Drive Car dataset generation."""
from random import random

import numpy as np
import pandas as pd

MIN_SPEED, MAX_SPEED = 0, 40  # Meters per second (144 kms per hour)
MIN_DISTANCE, MAX_DISTANCE = 0, 200  # Meters
MIN_FRICTION, MAX_FRICTION = 0.4, 0.8  # Coefficient
FREE_ROAD_PERCENTAGE = 0.6


def create_dataset(
        num_samples: int,
        min_speed: float = MIN_SPEED,
        max_speed: float = MAX_SPEED,
        min_distance: float = MIN_DISTANCE,
        max_distance: float = MAX_DISTANCE,
        min_friction: float = MIN_FRICTION,
        max_friction: float = MAX_FRICTION,
        free_road_percentage: float = FREE_ROAD_PERCENTAGE,
) -> pd.DataFrame:
    """
    Creates dataset based on parameters of the car, it's environment and amount of samples provided.

    Args:
        num_samples (int): number of samples to generate.
        max_speed (float): maximum possible speed of the car. Defaults to 150.
        min_speed (float): minimum possible speed of the car. Defaults to 0.
        min_distance (float): minimum distance in meters. Defaults to 0.
        max_distance (float): minimum distance in meters. Defaults to 0.
        min_friction (float): minimum road state friction. Defaults to 0.4.
        max_friction (float): maximum road state friction. Defaults to 0.8.
        free_road_percentage (float): percentage of the samples without distance to obstacles. Defaults to 0.6.

    Returns:
        pd.DataFrame: Generated dataframe.
    """
    data = {
        'distance_to_obstacle': np.round(
            MAX_DISTANCE if random() < free_road_percentage
            else np.random.uniform(min_distance, max_distance, num_samples)
        ).astype(float),

        'vehicle_speed': np.round(
            np.random.uniform(min_speed, max_speed, num_samples),
            decimals=3
        ),

        'friction': np.random.uniform(min_friction, max_friction, num_samples),  # Стан дороги
    }
    return pd.DataFrame(data)


if __name__ == '__main__':
    df = create_dataset(200)
    print(df)
