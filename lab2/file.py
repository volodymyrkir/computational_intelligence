import numpy as np
import pandas as pd
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import skfuzzy.control as ctrl

data = pd.DataFrame({
    'col1': [np.nan, np.nan, np.nan, np.nan, 52.257043, np.nan, np.nan, 8.105296, np.nan, np.nan],
    'col2': [82.787, 67.681, 87.071, 141.266, 51.203, 43.926, 21.979, 122.113, 79.683, 59.105],
    'col3': ['wet', 'wet', 'wet', 'dry', 'dry', 'wet', 'dry', 'wet', 'dry', 'dry']
})

# Replace NaN values with column mean (or use other imputation techniques)
data['col1'].fillna(data['col1'].mean(), inplace=True)

# Define the universe of discourse for col1 (input range)
speed = ctrl.Antecedent(data['col1'], 'speed')

# Define fuzzy membership functions for col1
col1_low = fuzz.trimf(speed.universe, [min(data['col1']), min(data['col1']), np.mean(data['col1'])])
col1_medium = fuzz.trimf(speed.universe, [min(data['col1']), np.mean(data['col1']), max(data['col1'])])
col1_high = fuzz.trimf(speed.universe, [np.mean(data['col1']), max(data['col1']), max(data['col1'])])

# Plot the membership functions
plt.figure()
plt.plot(speed.universe, col1_low, 'b', label='Low')
plt.plot(speed.universe, col1_medium, 'g', label='Medium')
plt.plot(speed.universe, col1_high, 'r', label='High')
plt.title('Fuzzy Membership Functions for col1')
plt.xlabel('col1')
plt.ylabel('Membership degree')
plt.legend()
plt.show()