import numpy as np
from scipy.interpolate import interp1d, CubicSpline, PchipInterpolator
from scipy.differentiate import derivative
import matplotlib.pyplot as plt
from Trajectory_1_Gen import keyframe

keyframe_array = np.array([keyframe["0"], # Takes the keyframe from Trajectory_Gen and sets it as a NumPy array to be transposed
                           keyframe["1"], 
                           keyframe["2"], 
                           keyframe["3"],
                           keyframe["4"],
                           keyframe["5"],
                           keyframe["6"],
                           keyframe["7"],
                           keyframe["8"],
                           keyframe["9"],
                           keyframe["10"]])

q_array = np.transpose(keyframe_array)  # Keyframe array is transposed so that each row represents the movement of a particular joint
q1_values = q_array[0]  # Definitions of each row
q2_values = q_array[1]
q3_values = q_array[2]
q4_values = q_array[3]
q5_values = q_array[4]
q6_values = q_array[5]
gripper1_values = q_array[6]
gripper2_values = q_array[7]

t_interp = np.linspace(0, 20, 11)  # Produces time matrix for linear interpolation
t_smooth = np.linspace(0, 20, 250)  # Produces time matrix for PCHIP interpolation  

q1_linear = interp1d(t_interp, q1_values)  # Linear interpolation of Q1 values 
q1_cubic = CubicSpline(t_interp, q1_values, bc_type = "natural")  # Cubic interpolation of Q1 values (for testing only)
q1_pchip = PchipInterpolator(t_interp, q1_values)  # PCHIP interpolation of Q1 values

q2_linear = interp1d(t_interp, q2_values)  # as before
q2_cubic = CubicSpline(t_interp, q2_values, bc_type = "natural")
q2_pchip = PchipInterpolator(t_interp, q2_values)

q3_linear = interp1d(t_interp, q3_values)
q3_cubic = CubicSpline(t_interp, q3_values, bc_type = "natural")
q3_pchip = PchipInterpolator(t_interp, q3_values)

q4_linear = interp1d(t_interp, q4_values)
q4_cubic = CubicSpline(t_interp, q4_values, bc_type = "natural")

q5_linear = interp1d(t_interp, q5_values)
q5_cubic = CubicSpline(t_interp, q5_values, bc_type = "natural")
q5_pchip = PchipInterpolator(t_interp, q5_values)

q6_linear = interp1d(t_interp, q6_values)
q6_cubic = CubicSpline(t_interp, q6_values, bc_type = "natural")

gripper1_linear = interp1d(t_interp, gripper1_values)
gripper1_pchip = PchipInterpolator(t_interp, gripper1_values)
gripper2_linear = interp1d(t_interp, gripper2_values)
gripper2_pchip = PchipInterpolator(t_interp, gripper2_values)
