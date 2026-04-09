## PURPOSE OF THE REPOSITORY ##
The files attached directly pertain to a BEng Honour's Project detailing the optimisation of a 6 DOF ViperX 300 articulated robotic arm for energy consumption.
This repository makes use of Python and the open-source engine MuJoCo for the simulations and data analysis of the robotic arm and its trajectories.

## CONTENTS ##
The files and folders in this repository take the following forms:

TRAJECTORY:
    - Trajectory_X_Gen.py : For the production of trajectory keys and the synthesis of keyframes
    - Interpolation_X.py : For the transposing of keyframes and the interpolation of q positions to form trajectory paths, where the interpolation methods are either Linear interpolation or Piecewise Cubic Hermite Interpolating Polynomial (PCHIP) interpolation
    - script_X.py : The main simulation script, which imports the data from the aforementioned scripts and uses MuJoCo to simulate them. The results of the scripts are then exported as .csv files for plotting

RESULTS:
    - csv_bin : Where the results data is exported to
    - E-P-Tau_Results: The matplotlib plots for Energy, Power and Torque
    - Q-V-A_Results: The matplotlib plots for joint position, joint velocity and joint acceleration
    - Traj_Box_Results: The matplotlib plots for variables pertaining to the movement of the payload, namely potential energy and cartesian position

For conciseness, the results for the optimised trajectory are contained in their own folder: "Final_Results".

## REQUIRED INSTALLMENTS ##
The files in this repository make use of Python directories and MuJoCo software which MUST be installed before running the simulations.

For this project the "-pip" method of installation was used for the following directories:
    - NumPy: For defining keys and keyframes
    - SciPy: For interpolation
    - Pandas: For exporting results
    - Matplotlib: For the production and viewing of plots
    - MuJoCo: For simulation 

## AUTHOR ##
Jason H. Lynass
School of Computing, Engineering and the Built Environment
Edinburgh Napier University
