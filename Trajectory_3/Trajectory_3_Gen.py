import numpy as np
import pandas as pd

# Starting Position
key_0 = np.array([0, -0.960, 1.160, 0, -0.300, 0, 0.057, -0.057])

# Waist Extended
key_1 = np.array([1.57, -0.215, 0.475, 0, 0.400, 0, 0.057, -0.057])

# Descent
key_2 = np.array([1.57, 0.52, -0.22, 0, 1.1, 0, 0.057, -0.057])

# Close Gripper
key_3 = np.array([1.57, 0.52, -0.22, 0, 1.1, 0, 0.021, -0.021])

# Elevate
key_4 = np.array([1.57, 0.34, -0.33, 0, 1.39, 0, 0.021, -0.021])

# Rotate
key_5 = np.array([1.05, 0.34, -0.33, 0, 1.39, 0, 0.021, -0.021])

# Rotate
key_6 = np.array([0.52, 0.34, -0.33, 0, 1.39, 0, 0.021, -0.021])

# Rotate
key_7 = np.array([0, 0.34, -0.33, 0, 1.39, 0, 0.021, -0.021])

# Rotate
key_8 = np.array([-0.52, 0.34, -0.33, 0, 1.39, 0, 0.021, -0.021])

# Rotate
key_9 = np.array([-1.05, 0.34, -0.33, 0, 1.39, 0, 0.021, -0.021])

# Rotate
key_10 = np.array([-1.57, 0.34, -0.33, 0, 1.39, 0, 0.021, -0.021])

# Placing
key_11 = np.array([-1.57, 0.52, -0.22, 0, 1.1, 0, 0.021, -0.021])

# Open Gripper
key_12 = np.array([-1.57, 0.52, -0.22, 0, 1.1, 0, 0.057, -0.057])

# Waist Extended
key_13 = np.array([-1.57, -0.215, 0.475, 0, 0.400, 0, 0.057, -0.057])

# Starting Position
key_14 = np.array([0, -0.960, 1.160, 0, -0.300, 0, 0.057, -0.057])

keyframe = {"0": key_0,
            "1": key_1,
            "2": key_2,
            "3": key_3,
            "4": key_4,
            "5": key_5,
            "6": key_6,
            "7": key_7,
            "8": key_8,
            "9": key_9,
            "10": key_10,
            "11": key_11,
            "12": key_12,
            "13": key_13,
            "14": key_14}

if __name__ == "__main__":
    print()
    print("-------GENERATED KEYFRAME-------")
    keyframe_series = pd.Series(keyframe)
    print(keyframe_series)
